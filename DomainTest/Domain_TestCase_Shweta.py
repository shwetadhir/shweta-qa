'''
Using Cypress/Selenium Webdriver, write a script to automate the following test
scenario:
1. Open website https://www.domain.com.au
2. Click on all main nav options > Buy, Rent, New Homes, Sold, Rural
3. This script should be able to verify all the pages have been loaded successfully.
4. Make sure the validations/assertions are effective.
'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import re
import time
import sys
import json
import sys
import urllib.request

testData = {
    "HomepageUrl" : "https://www.domain.com.au",
    "HomepageHeadline" : "Search Australia's home of property",
    "NavHeadlines" : {'Buy':"Search Australia's home of property",'Rent':"Search Australia's home of property",'New Homes':"Search Australia's home of property",'Sold':"Search Australia's home of property",'Rural':"Find Rural Property in Australia"}
}


Homepage = testData["HomepageUrl"]

error = ""
try:
    response = urllib.request.urlopen(Homepage)
    code = response.getcode()
except urllib.error.URLError as e:
    error = e.reason

if(error == "") and (code == 200):

    driver = webdriver.Firefox(executable_path='C:\SoftwaresInstalled\geckodriver.exe')
    print('Connecting website - Successful')
    print('Browser open')
    driver.get(Homepage)

    expectedHeadline = testData["HomepageHeadline"]
    headline = driver.find_element_by_css_selector("h1.domain-home__headline").get_attribute('textContent')

    if headline==expectedHeadline:
        print(Homepage + ' loaded successfully')

        headlines = testData["NavHeadlines"]
        for navButton in driver.find_elements_by_css_selector("div.search-box-a .search-box-a__search-mode-nav>button"):
            text = navButton.get_attribute('textContent')
            navButton.click()
            time.sleep(5)
            headline = driver.find_element_by_css_selector("h1.domain-home__headline").get_attribute('textContent')
            if headline == headlines[text]:
                print('"' + text + '" link loaded successfully')
            else:
                print('Unable to load "'+ text +'" link correctly (missing expected headline)')

    else:
        print('Unable to load homepage correctly (missing expected headline)')

    driver.quit()
    print('Browser closed')
else:
    print("Unable to open webpage: " + Homepage)
    print("Error: " + str(error))