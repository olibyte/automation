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
bb_ids = ['SCWK90064_2019_FEB', 'AUDI90004_2019_YRL']
canvas_ids = ['PSYT90104_2020_SEP', 'PHTY90109_2020_JUL']

enrolee_id = users[2]
peer_id = peers[1]

testers = ['oliverb2', 'droker']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized") 
maximize = webdriver.ChromeOptions()
maximize.add_argument('--start-maximized')

# jira = webdriver.Chrome(chrome_options=chrome_options)
# jira.get('https://uomouajv.atlassian.net/')

# time.sleep(2)
# jira_email_input = jira.find_element_by_id('username')
# jira_email_input.send_keys(email)
# jira.find_element_by_id('login-submit').submit()
# jira_password_input = jira.find_element_by_id('password')
# time.sleep(1)
# jira_password_input.send_keys(password + Keys.RETURN)

#LAUNCH BROWSERS

blackboard = webdriver.Firefox()
canvas = webdriver.Chrome(chrome_options=maximize)

#GO TO HOMEPAGES
blackboard.get('https://app.lms.unimelb.edu.au/')
blackboard.maximize_window()
canvas.get('https://lms.unimelb.edu.au/canvas')

#LOGIN TO CANVAS
try:
    canvas.find_element_by_id('consent_prompt_submit').click()
finally:
    time.sleep(2)
canvas.get('https://canvas.lms.unimelb.edu.au/login/saml')

time.sleep(2)
auth_user = canvas.find_element_by_id('usernameInput')
auth_password = canvas.find_element_by_id('passwordInput')
# 
auth_user.send_keys(user_id)
auth_password.send_keys(password)
auth_password.send_keys(Keys.RETURN)
time.sleep(2)
# 
#LOGIN TO BLACKBOARD
bb_user = blackboard.find_element_by_id('user_id')
bb_password = blackboard.find_element_by_id('password')
blackboard.implicitly_wait(5)
bb_user.send_keys(user_id)
bb_password.send_keys(password)
bb_password.send_keys(Keys.RETURN)

#BEGIN CANVAS ENROLMENT LOOP
 
#CANVAS CONSOLE
canvas.get('https://canvas.lms.unimelb.edu.au/accounts/1?')
time.sleep(3)
#GET RID OF THE PROMPT
try:
    ask_me_later = canvas.find_element_by_css_selector('#wm-shoutout-159266 > div.wm-content > div.buttons-wrapper > span')
    ask_me_later.click()
except:
    print('no prompt')
#TRAVERSE THROUGH SUBJECTS AND ADD THE ENROLEE
for x in canvas_ids:
    time.sleep(2)
    canvas.get('https://canvas.lms.unimelb.edu.au/accounts/1?')
    time.sleep(2)
    canvas_search = canvas.find_element_by_xpath("//input[@placeholder='Search subjects...']")
    canvas_search.send_keys(x)
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
#END CANVAS ENROLMENT LOOP


# blackboard.get('https://app.lms.unimelb.edu.au/webapps/blackboard/execute/coursemanager?sourceType=COURSES')
#BLACKBOARD CONSOLE
for x in bb_ids:
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
        courseInfoSearchText.clear()
        time.sleep(2)
        courseInfoSearchText.send_keys(x, Keys.RETURN)
        time.sleep(10)
    #SEARCHING...WAIT UNTIL THE LIST RENDERS THEN CLICK THE FIRST SUBJECT LISTED.
    try:
        element= WebDriverWait(blackboard, 10).until(
            EC.presence_of_element_located((By.ID, "listContainer_datatable")) #expected condition
            )
    finally:
        blackboard.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[3]/form/div[2]/div[3]/div/table/tbody/tr/td[2]/span[2]/a').click()
    #UNCOMMENT THIS BLOCK IF YOU NEED TO BE ENROLLED
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
    #JUMP HERE IF YOU'RE ALREADY ENROLLED
    try:
        element= WebDriverWait(blackboard, 10).until(
            EC.presence_of_element_located((By.ID, 'anonymous_element_16'))
        )
        
    finally:
        blackboard.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        blackboard.find_element_by_link_text('Users and Groups').click()
        time.sleep(1)
         
    try:
        blackboard.find_element_by_link_text('Staff Roles').click()
    # finally:
        # blackboard.find_element_by_css_selector('#controlpanel\.users\.and\.groups_groupContents > li:nth-child(4) > a:nth-child(1)').click()
    
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
        pattern = blackboard.find_element_by_id('pattern')
        pattern.clear()
        time.sleep(1)
        pattern.send_keys(enrolee_id, Keys.RETURN)
    try:
        element= WebDriverWait(blackboard, 10).until(
            EC.presence_of_element_located((By.ID, 'listContainer_databody'))
        )
    finally:
        chevron = blackboard.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/table/tbody/tr/td[1]/span[2]/span/a')

        chevron.click()
        chevron.send_keys(Keys.ARROW_DOWN, Keys.RETURN)

        # element= WebDriverWait(blackboard, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/ul/li[2]/a'))
        # )
        # blackboard.find_element_by_xpath('/html/body/div[6]/ul/li[2]/a').click()

        element= WebDriverWait(blackboard, 10).until(
            EC.presence_of_element_located((By.ID, 'Sys Admin'))
        )
        blackboard.find_element_by_css_selector('#Sys\ Admin > a:nth-child(1)').click()
        