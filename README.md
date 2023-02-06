# Release Notes Generator

This code is a Python script that generates release notes from the issues in a JIRA project that
have been resolved in a specific date range.

The date range is specified as a command-line argument in the format YYYY-MM-DD. The script uses the
Selenium library to interact with the JIRA web interface and the Chrome browser.

## Requirements

- Python 3.x
- Selenium
- Chrome Webdriver

## How to run script

1. Download Python from this [Link](https://www.python.org/downloads/) and install it. When you run
   downloaded package it is important to check box **"Add python.exe to PATH"** in order to set
   environment variables automatically.
2. Clone this git repo using command `git clone https://github.com/nikolamirilo/Release_Notes_Generator.git`
3. Open project in VS Code
4. Open Terminal
5. Run command `pip install selenium`
6. Enter your credentials in `secrets.py` file
7. Run the script using `python main.py <sprintStartDate> <sprintEndDate>`, where sprintStartDate
   and sprintEndDate are in format YYYY-MM-DD. Example: `python main.py "2023-01-23" "2023-02-01"`
8. The release notes will be downloaded as an Excel file.
