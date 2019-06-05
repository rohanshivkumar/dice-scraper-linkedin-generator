from selenium import webdriver
import time
import re
import os
import traceback
import csv
import json
import random
import urllib
import time
from googleapiclient.discovery import build
import tkinter as Tk
my_api_key = ""  # Enter Your Google API Key
my_cse_id = ""  # Enter Your Google Custom Search Engine ID
my_chromedriver_path = ""  # Enter the path to your chromedriver executable

options = webdriver.ChromeOptions()
options.add_argument('--headless') #Makes chrome headless to save cpu and ram resources
options.add_argument('--disable-gpu')
browser = webdriver.Chrome(my_chromedriver_path, chrome_options=options)
browser.implicitly_wait(10)


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    print(search_term)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    results = []
    try:
        for item in res['items']:
            if("linkedin.com" in item['link'] and "linkedin.com/jobs" not in item['link']
               and "linkedin.com/userp" not in item['link']
               and "linkedin.com/title" not in item['link']):
                results.append(item['link'])
        return results
    except KeyError:
        return results


def parse(keyword, place):
    csv_file = '%s-%s-dice-job-results.csv' % (keyword, place)
    job_listings = []
    fieldnames = ['Name', 'Company', 'Location', 'Url', 'LinkedIn']
    csvfile = open(csv_file, "w")
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    csvfile.close()
    job_base_url = 'https://www.dice.com/jobs?'
    data = {
        'q': keyword,
        'l': place
    }
    job_search_url = job_base_url + urllib.parse.urlencode(data)
    try:
        i = 0
        browser.get(job_search_url)
        while(i < 3):
            page_listings = []
            csvfile = open(csv_file, "a")
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if(i != 0 and next_url):
                link = next_url
                browser.get(link)
            XPATH_ALL_JOB = '//div[@class="complete-serp-result-div"]'
            company_suffix = '//span[@class="hidden-xs"]//span[@class="compName"]'
            name_suffix = '//a/span'
            job_url_suffix = '//a[@href]'
            loc_suffix = '//span[@class="jobLoc"]'
            i += 1
            next_url = job_search_url + "&p=%s" % (i+1)
            print(next_url)
            listings = browser.find_elements_by_xpath(XPATH_ALL_JOB)
            j = 1
            print("Scraping page %s" % i)
            for job in listings:
                XPATH_NAME = XPATH_ALL_JOB + "[%s]" % j + name_suffix
                XPATH_JOB_URL = XPATH_ALL_JOB + "[%s]" % j + job_url_suffix
                XPATH_LOC = XPATH_ALL_JOB + "[%s]" % j + loc_suffix
                XPATH_COMPANY = XPATH_ALL_JOB + "[%s]" % j + company_suffix
                job_name = browser.find_element_by_xpath(XPATH_NAME).text
                job_location = browser.find_element_by_xpath(XPATH_LOC).text
                job_url = browser.find_element_by_xpath(
                    XPATH_JOB_URL).get_attribute("href")
                company_name = browser.find_element_by_xpath(
                    XPATH_COMPANY).text
                job_key = job_name + "-" + company_name + "-" + job_location
                if(job_key in job_listings):
                    continue
                search_term = company_name + " " + job_name + \
                    ' \"manager\" OR \"director\" linkedIn'
                #linkedinurl = google_search(search_term, my_api_key, my_cse_id, num=10,siteSearch = "linkedin.com")
                jobs = {
                    "Name": job_name,
                    "Company": company_name,
                    "Location": job_location,
                    "Url": job_url,
                    #"LinkedIn": linkedinurl
                }
                job_listings.append(job_key)
                page_listings.append(jobs)
                writer.writerow(jobs)
                time.sleep(random.randint(1, 3))
                j += 1
            print("Done with page %s, taking a break " % i)

            csvfile.close()
            time.sleep(20)
        browser.quit()
        return page_listings
    except Exception:
        print("Error occured scraping Dice")
        print(traceback.print_exc())
        browser.quit()
        return False


parse("tech support","santa clara,ca")