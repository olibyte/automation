#this script launches blackboard and jira in incognito mode, and canvas in regular mode.
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://app.lms.unimelb.edu.au/')

browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('https://uomouajv.atlassian.net/')

another = webdriver.Chrome()
another.get('https://lms.unimelb.edu.au/canvas')