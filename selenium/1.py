#this script launches blackboard and jira in incognito mode, and canvas in regular mode.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

password = ''
email = ''
user_id = ''
bb_source_id = ''
canvas_source_id = ''

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito --start-maximized")

maximize = webdriver.ChromeOptions()
maximize.add_argument('--start-maximized')

# blackboard = webdriver.Chrome(chrome_options=chrome_options)
# blackboard.get('https://app.lms.unimelb.edu.au/')
# 
jira = webdriver.Chrome(chrome_options=chrome_options)
jira.get('https://uomouajv.atlassian.net/')

time.sleep(2)
jira_email_input = jira.find_element_by_id('username')
jira_email_input.send_keys(email)
jira.find_element_by_id('login-submit').submit()
jira_password_input = jira.find_element_by_id('password')
time.sleep(1)
jira_password_input.send_keys(password + Keys.RETURN)
# 
# canvas = webdriver.Chrome(chrome_options=maximize)
# canvas.get('https://lms.unimelb.edu.au/canvas')
# time.sleep(1)
# canvas.find_element_by_id('consent_prompt_submit').click()
# time.sleep(1)
# canvas.get('https://canvas.lms.unimelb.edu.au/login/saml')
# time.sleep(2)
# auth_user = canvas.find_element_by_id('usernameInput')
# auth_password = canvas.find_element_by_id('passwordInput')
# 
# auth_user.send_keys(user_id)
# auth_password.send_keys(password)
# auth_password.send_keys(Keys.RETURN)
# time.sleep(1)
# canvas.get('https://canvas.lms.unimelb.edu.au/accounts/1?')
# time.sleep(2)
# ask_me_later = canvas.find_element_by_css_selector('#wm-shoutout-159266 > div.wm-content > div.buttons-wrapper > span')
# ask_me_later.click()
# time.sleep(1)
# canvas_search = canvas.find_element_by_xpath("//input[@placeholder='Search subjects...']")
# canvas_search.send_keys('ABC')
# time.sleep(2)
# 
# find search box
# bb_user = blackboard.find_element_by_id('user_id')
# bb_password = blackboard.find_element_by_id('password')
# time.sleep(1)
# bb_user.send_keys(user_id)
# bb_password.send_keys(password)
# bb_password.send_keys(Keys.RETURN)
# time.sleep(2)
# blackboard.find_element_by_id('nav_list_courses').click()
# time.sleep(1)
# courseInfoSearchKeyString = Select(blackboard.find_element_by_id('courseInfoSearchKeyString'))
# courseInfoSearchKeyString.select_by_visible_text('Subject ID')
# courseInfoSearchText = blackboard.find_element_by_id('courseInfoSearchText')
# how to read in BB source IDs?
# courseInfoSearchText.send_keys(canvas_source_id)




