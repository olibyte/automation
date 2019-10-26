#this script launches blackboard and jira in incognito mode, and canvas in regular mode.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

password = ''
email = ''
user_id = 'oliverb2'

users = ['atiak', 'droker','oliverb2','senhaoz1', 'mckew', 'akinyokuno', 'naranetaalan', 'hitoa', 'duricg', 'smitss', 'drummondk']
checkers = ['senhaoz1', 'mckew', 'akinyokuno', 'naranetaalan', 'hitoa', 'duricg']
peers =  ['smitss','drummondk']

bb_source_id = 'SCWK90038_2019_AUG'
canvas_source_id = 'SCWK90038_2020_AUG'
bb_ids = ['SCWK90038_2019_AUG', 'SCWK90065']
canvas_ids = ['Playpen: Oliver Bennett', 'Playpen: Atia Kabir']
enrolee_id = users[6]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# 
maximize = webdriver.ChromeOptions()
maximize.add_argument('--start-maximized')

blackboard = webdriver.Firefox()
blackboard.get('https://app.lms.unimelb.edu.au/')
# 
# jira = webdriver.Chrome(chrome_options=chrome_options)
# jira.get('https://uomouajv.atlassian.net/')

# time.sleep(2)
# jira_email_input = jira.find_element_by_id('username')
# jira_email_input.send_keys(email)
# jira.find_element_by_id('login-submit').submit()
# jira_password_input = jira.find_element_by_id('password')
# time.sleep(1)
# jira_password_input.send_keys(password + Keys.RETURN)
# 
# ADD A USER TO CANVAS
canvas = webdriver.Chrome(chrome_options=maximize)
canvas.get('https://lms.unimelb.edu.au/canvas')
try:
    canvas.find_element_by_id('consent_prompt_submit').click()
finally:
    time.sleep(2)
canvas.get('https://canvas.lms.unimelb.edu.au/login/saml')
# canvas.find_element_by_xpath('//*[@id="main-content"]/section[1]/ul/li[1]/a/span').click()
time.sleep(2)
auth_user = canvas.find_element_by_id('usernameInput')
auth_password = canvas.find_element_by_id('passwordInput')

auth_user.send_keys(user_id)
auth_password.send_keys(password)
auth_password.send_keys(Keys.RETURN)
time.sleep(2)

canvas.get('https://canvas.lms.unimelb.edu.au/accounts/1?')
time.sleep(3)
ask_me_later = canvas.find_element_by_css_selector('#wm-shoutout-159266 > div.wm-content > div.buttons-wrapper > span')
ask_me_later.click()
time.sleep(2)
canvas_search = canvas.find_element_by_xpath("//input[@placeholder='Search subjects...']")
canvas_search.send_keys(canvas_source_id)
time.sleep(2)
target_subject = canvas.find_element_by_xpath('//*[@id="content"]/div/table/tbody/tr/td[1]/a').click()
time.sleep(2)
canvas.find_element_by_xpath('//*[@id="section-tabs"]/li[10]/a').click()
time.sleep(2)
canvas.find_element_by_id('addUsers').click()
time.sleep(2)
canvas_add_user_textarea = canvas.find_element_by_xpath('//*[@id="add_people_modal"]/div[2]/div/div/fieldset[2]/label/span/span[1]/span[2]/div/textarea')
time.sleep(2)
canvas_add_user_textarea.send_keys(enrolee_id, Keys.TAB, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.RETURN)
time.sleep(1)
canvas.find_element_by_id('addpeople_next').click()
time.sleep(0.5)
canvas.find_element_by_id('addpeople_next').click()

# find search box
bb_user = blackboard.find_element_by_id('user_id')
bb_password = blackboard.find_element_by_id('password')
blackboard.implicitly_wait(5)
bb_user.send_keys(user_id)
bb_password.send_keys(password)
bb_password.send_keys(Keys.RETURN)

# blackboard.get('https://app.lms.unimelb.edu.au/webapps/blackboard/execute/coursemanager?sourceType=COURSES')

try:
    element= WebDriverWait(blackboard, 10).until(
        EC.presence_of_element_located((By.ID, "nav_list_courses")) #expected condition
        )
finally:
    blackboard.find_element_by_id('nav_list_courses').click()
try:
    element=WebDriverWait(blackboard,10).until(
        EC.presence_of_element_located((By.ID, 'courseInfoSearchKeyString'))
    )
finally:
    courseInfoSearchKeyString = Select(blackboard.find_element_by_id('courseInfoSearchKeyString'))
courseInfoSearchKeyString.select_by_visible_text('Subject ID')
courseInfoSearchText = blackboard.find_element_by_id('courseInfoSearchText')
# how to read in BB source IDs?
courseInfoSearchText.send_keys(bb_source_id, Keys.RETURN)

try:
    element= WebDriverWait(blackboard, 10).until(
        EC.presence_of_element_located((By.ID, "listContainer_datatable")) #expected condition
        )
finally:
    # try:
    blackboard.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[3]/form/div[2]/div[3]/div/table/tbody/tr/td[2]/span[2]/a').click()
    # finally:
    #     blackboard.find_element_by_css_selector('.nowrapCell > span:nth-child(2) > a:nth-child(1)').click()
# try:
    # element= WebDriverWait(blackboard, 10).until(
        # EC.presence_of_element_located((By.ID, "quickEnrollLink")) #expected condition
        # )
# finally:
    # blackboard.find_element_by_id('quickEnrollLink').click()
# try:
    # alert = blackboard.switch_to_alert()
    # alert.accept()
    # print("alert accepted")
# except:
    # print("no alert")
try:
    element= WebDriverWait(blackboard, 10).until(
        EC.presence_of_element_located((By.ID, 'anonymous_element_16'))
    )
finally:
    blackboard.find_element_by_link_text('Users and Groups').click()
    time.sleep(1)
    blackboard.find_element_by_link_text('Staff Roles').click()
try:
    element= WebDriverWait(blackboard, 10).until(
        EC.presence_of_element_located((By.ID, 'nav'))
    )
finally:
    blackboard.find_element_by_css_selector('#nav > li:nth-child(1) > a:nth-child(1)').click()
try:
    element= WebDriverWait(blackboard, 10).until(
        EC.presence_of_element_located((By.ID, 'pattern'))
    )
finally:
    blackboard.find_element_by_id('pattern').send_keys(enrolee_id, Keys.RETURN)
try:
    element= WebDriverWait(blackboard, 10).until(
        EC.presence_of_element_located((By.ID), 'listContainer_databody')
    )
finally:
    blackboard.find_element_by_xpath('//*[@title="options"]').click()