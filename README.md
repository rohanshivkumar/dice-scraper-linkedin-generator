Searches for jobs in certain locations from glassdoor, finds LinkedIn of potential connections related to the job searched for. Writes to .csv file in the directory of download in the format jobname-location-results.csv(Example: tech support-san jose-job-results.csv)

Uses selenium for automated browsing to scrape data.
Requires python 3.6 to be installed on system with PATH variable set. 

INSTALLATION
1. Clone or Download the repository to a folder.

2. In command prompt, navigate to the folder and run the following command: pip install -r requires.txt

3a. (FOR GOOGLE CHROME AS BROWSER) Head to http://chromedriver.chromium.org/downloads and download the webdriver corresponding to your chrome version and add this file's location to your system environment variable (PATH).

3b. (FOR SAFARI AS BROWSER) 
High Sierra and later:
Run `safaridriver --enable` once. (If you’re upgrading from a previous macOS release, you may need to use sudo.)

Sierra and earlier:
If you haven’t already done so, make the Develop menu available. Choose Safari > Preferences, and on the Advanced tab, select “Show Develop menu in menu bar.” For details, see https://support.apple.com/guide/safari/welcome.
Choose Develop > Allow Remote Automation.
Authorize safaridriver to launch the XPC service that hosts the local web server. To permit this, manually run /usr/bin/safaridriver once and follow the authentication prompt.
4. Open up "safari_dice_linkedin.py" or "chrome_dice_linkedin.py"in a text editor and edit lines 13,14 to match your google API key, custom search engine ID (my_api_key = "" #Enter Your Google API Key my_cse_id = "" #Enter Your Google Custom Search Engine ID)
If using chrome, in "chrome_dice_linkedin.py" edit line 15 and add the path to the downloaded chrome driver (my_chromedriver_path = ""  # Enter the path to your chromedriver executable)


USAGE

Windows: Double click "safari_dice_linkedin.py" or "chrome_dice_linkedin.py" file to run the file. OR In command line run "python path/to/"safari_dice_linkedin.py" (OR) "chrome_dice_linkedin.py".py" (Replace path/to/ with the actual path of your download file)

Mac OSX: Right click and open with Python Launcher to run the file. OR In command line run "python path/to/"safari_dice_linkedin.py" (OR) "chrome_dice_linkedin.py" (Replace path/to/ with the actual path of your download file)

Linux: In command line run "python path/to/"safari_dice_linkedin.py" (OR) "chrome_dice_linkedin.py" (Replace path/to/ with the actual path of your download file)

Enter job name and location in appropriate entry boxes and press "Find jobs" button.
