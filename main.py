import argparse
import time
from secrets import password, username

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
jql = f"project = \"LJ ADI IMPL DVA\" AND status = Done AND resolved >= \"{sprintStartDate}\" AND resolved < \"{sprintEndDate}\" and resolution = Fixed  and issuetype in (Task, Improvement)"

class GenerateReleaseNotes:
    def __init__(self):
        self.url = "https://jira.adacta-fintech.com/login.jsp"
        self.username = username
        self.password = password
        c = Options()
        c.add_argument("--headless")
        self.browser = webdriver.Chrome()
    def login(self):
        # Open the JIRA login page
        self.browser.get(self.url)
        self.browser.minimize_window()
        time.sleep(1)
        # Enter the username and password
        username_field = self.browser.find_element(By.ID, "login-form-username")
        password_field = self.browser.find_element(By.ID, "login-form-password")
        username_field.send_keys(self.username)
        password_field.send_keys(self.password)
        # Click the "Log In" button
        login_button = self.browser.find_element(By.ID, "login-form-submit")
        login_button.click()
    def getData(self):
        self.browser.get("https://jira.adacta-fintech.com/issues/?jql=")
        time.sleep(1)
        jql_field = self.browser.find_element(By.ID,"advanced-search")
        jql_field.send_keys(jql)
        time.sleep(1)
        searchButton = self.browser.find_element(By.CLASS_NAME, "search-button")
        searchButton.click()
        time.sleep(1)
        #Export excel file with current fields
        export_button = self.browser.find_element(By.ID, "AJS_DROPDOWN__81")
        export_button.click()
        time.sleep(1)
        current_fields_button = self.browser.find_element(By.ID, "currentExcelFields")
        current_fields_button.click()
        time.sleep(1)
        print("Downloaded Release Notes")
        self.browser.close()
main = GenerateReleaseNotes()
main.login()
main.getData()

