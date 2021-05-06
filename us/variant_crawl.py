# Web crawler for CDC Tableau dashboards to download data.
# Currently only supports the CDC Variant dashboard, but the
# principles will work with any Tableau Public dashboard.
# Written by chrwang in May 2021
import time
import urllib.request
import argparse
import os
import glob
import filecmp
import datetime

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains

TEMP_FILE = "0temp.csv"

parser = argparse.ArgumentParser(description='Downloads the CDC variant file for the current day.')
parser.add_argument('dl_path', type=str, help="directory to download fiels to")

# Check if the most recently named file in the directly has the same file contents
# as the file we just downloaded. If it does, remove the temp file and exit.
# Otherwise, this means we have an updated CSV. Name it to today's date and keep it.
def cmp_and_swap(path):
    files = sorted([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    most_recent = files[-1]

    if filecmp.cmp(os.path.join(path, most_recent), os.path.join(path, TEMP_FILE)):
        os.remove(os.path.join(path, TEMP_FILE))
    else:
        os.rename(os.path.join(path, TEMP_FILE), os.path.join(path, datetime.datetime.today().strftime("%Y-%m-%d") + ".csv"))

# Web crawler function.
def main(dl_path):
    # Run Firefox headless
    opts = Options()
    opts.headless = True
    prof = webdriver.FirefoxProfile()

    # Don't show download dialog for CSV files
    prof.set_preference('browser.download.folderList', 2)
    prof.set_preference('browser.download.manager.showWhenStarting', False)
    prof.set_preference('browser.download.dir', '/tmp')
    prof.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

    with webdriver.Firefox(prof, options=opts, log_path="/tmp/geckodriver.log") as driver:
        # Initialise the driver
        ac = ActionChains(driver)
        driver.get("https://public.tableau.com/views/State_Proportions_table/StateProportionsDash?%3Alanguage=en&%3Aembed=y&%3AshowVizHome=no&%3Adisplay_count=y&%3Arender=false")
        print("Using page " + driver.title)
        # Wait for page to load
        time.sleep(10)

        # Click the left sidebar twice to activate downloads
        state_button = driver.find_element_by_class_name("tab-clip")
        az_btn = driver.find_elements_by_class_name("tvimagesContainer")[0]
        ac.move_to_element(az_btn).click().perform()
        time.sleep(5)
        az_btn.click()
        time.sleep(5)

        # Click the download button
        dl_btn = driver.find_element_by_class_name("tab-icon-download")
        dl_btn.click()

        # Click the Data button in the download menu
        data_btn = driver.find_element_by_xpath('//*[@class="tab-downloadDialog"]/fieldset/button[2]')
        data_btn.click()

        # Attempt to switch to the new donwload popup
        owh = driver.current_window_handle
        for nwh in driver.window_handles:
            if nwh != owh:
                driver.switch_to_window(nwh)
                break
        if owh == driver.current_window_handle:
            print("An error occurred when switching to the download popup.")
            exit(1)

        # Wait for the popup to load
        time.sleep(5)

        # Switch to the Full Data tab
        fd_btn = driver.find_element_by_xpath('//*[@id="tab-view-table-data-0"]')
        fd_btn.click()
        time.sleep(5)

        # Grab the data from the download all link
        dl_all = driver.find_element_by_class_name('csvLink')
        dl_url = dl_all.get_attribute("href")
        urllib.request.urlretrieve(dl_url, os.path.abspath(os.path.join(dl_path, TEMP_FILE)))

        # Check and rename tmp if it appears different
        cmp_and_swap(dl_path)

if __name__ == "__main__":
    args = parser.parse_args()
    main(args.dl_path)
