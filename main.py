import argparse
import time
from secrets import password, username

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Parse the sprintStartDate and sprintEndDate from the command-line argument
parser = argparse.ArgumentParser()
parser.add_argument("sprintStartDate", help="The sprintStartDate to be entered in the JQL command in format YYYY-MM-DD")
parser.add_argument("sprintEndDate", help="The sprintEndDate to be entered in the JQL command in format YYYY-MM-DD")
args = parser.parse_args()
sprintStartDate = args.sprintStartDate
sprintEndDate = args.sprintEndDate

# JQL command
jql = f"project = \"LJ ADI IMPL DVA\" AND status in (Done, Closed) AND resolved >= \"{sprintStartDate}\" AND resolved < \"{sprintEndDate}\" AND comment ~ \"merge request\" and resolution = Fixed  and issuetype in (Task, Improvement) ORDER BY resolved ASC"

class GenerateReleaseNotes:
    def __init__(self):
        self.url = "https://jira.adacta-fintech.com/login.jsp"
        self.username = username
        self.password = password
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--enable-javascript")
        self.driver = webdriver.Firefox(options=options)
        print("\033[32mFinished with webdirver setup\033[0m")
    def login(self):
        # Open the JIRA login page
        self.driver.get(self.url)
        time.sleep(1)
        print("\033[32mReached: https://jira.adacta-fintech.com\033[0m")
        # Enter the username and password
        username_field = self.driver.find_element(By.ID, "login-form-username")
        password_field = self.driver.find_element(By.ID, "login-form-password")
        username_field.send_keys(self.username)
        password_field.send_keys(self.password)
        # Click the "Log In" button
        login_button = self.driver.find_element(By.ID, "login-form-submit")
        login_button.click()
        print("\033[32mSuccessfully logged in\033[0m")
    def getData(self):
        self.driver.get("https://jira.adacta-fintech.com/issues/?jql=")
        time.sleep(1)
        jql_field = self.driver.find_element(By.ID,"advanced-search")
        jql_field.send_keys(jql)
        time.sleep(1)
        searchButton = self.driver.find_element(By.CLASS_NAME, "search-button")
        searchButton.click()
        time.sleep(1)
        #Export excel file with current fields
        export_button = self.driver.find_element(By.ID, "AJS_DROPDOWN__81")
        export_button.click()
        time.sleep(1)
        current_fields_button = self.driver.find_element(By.ID, "currentExcelFields")
        current_fields_button.click()
        time.sleep(1)
        print("\033[32mSuccessfully downloaded Release Notes!\033[0m")
        self.driver.close()
main = GenerateReleaseNotes()
main.login()
main.getData()

