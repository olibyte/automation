import requests
import time
import json
import jira
#JQL queries.
all_canvas_id = 'https://uomouajv.atlassian.net/rest/api/3/search?jql=project%20%3D%20CSM%20AND%20issuetype%20%3D%20Subject%20AND%20status%20in%20("1.%20Selected%20for%20Action"%2C%20Backlog)%20AND%20resolution%20%3D%20Unresolved%20AND%20"Auto%20Migration%20Status"%20%3D%20Success%20AND%20Faculty%20in%20("Architecture%2C%20Building%20and%20Planning"%2C%20"Medicine%2C%20Dentistry%20and%20Health%20Sciences")%20AND%20assignee%20in%20(EMPTY%2C%20atia.kabir%2C%20oliver.bennett())%20ORDER%20BY%20priority%20DESC&fields=customfield_12231'
all_bb_id = 'https://uomouajv.atlassian.net/rest/api/3/search?jql=project%20%3D%20CSM%20AND%20issuetype%20%3D%20Subject%20AND%20status%20in%20("1.%20Selected%20for%20Action"%2C%20Backlog)%20AND%20resolution%20%3D%20Unresolved%20AND%20"Auto%20Migration%20Status"%20%3D%20Success%20AND%20Faculty%20in%20("Architecture%2C%20Building%20and%20Planning"%2C%20"Medicine%2C%20Dentistry%20and%20Health%20Sciences")%20AND%20assignee%20in%20(EMPTY%2C%20atia.kabir%2C%20currentUser())%20ORDER%20BY%20priority%20DESC&fields=customfield_12266'

all_peers_canvas = 'https://uomouajv.atlassian.net/rest/api/3/search?jql=project%20%3D%20CSM%20AND%20issuetype%20%3D%20Subject%20AND%20status%20%3D%20"2.%20Comparative%20Check%20%26%20Fixes"%20AND%20resolution%20%3D%20Unresolved%20AND%20"Auto%20Migration%20Status"%20%3D%20Success%20AND%20Faculty%20in%20("Architecture%2C%20Building%20and%20Planning"%2C%20"Medicine%2C%20Dentistry%20and%20Health%20Sciences")%20AND%20assignee%20in%20(atia.kabir%2C%20oliver.bennett()%2C%20EMPTY)%20AND%20"Peer%20Reviewer"%20in%20(EMPTY)%20ORDER%20BY%20priority%20DESC&fields=customfield_12231'
all_peers_bb = 'https://uomouajv.atlassian.net/rest/api/3/search?jql=project%20%3D%20CSM%20AND%20issuetype%20%3D%20Subject%20AND%20status%20%3D%20"2.%20Comparative%20Check%20%26%20Fixes"%20AND%20resolution%20%3D%20Unresolved%20AND%20"Auto%20Migration%20Status"%20%3D%20Success%20AND%20Faculty%20in%20("Architecture%2C%20Building%20and%20Planning"%2C%20"Medicine%2C%20Dentistry%20and%20Health%20Sciences")%20AND%20assignee%20in%20(atia.kabir%2C%20oliver.bennett()%2C%20EMPTY)%20AND%20"Peer%20Reviewer"%20in%20(EMPTY)%20ORDER%20BY%20priority%20DESC&fields=customfield_12266'

#Find peer reviews:
query = 'jql=project%20%3D%20CSM%20AND%20issuetype%20%3D%20Subject%20AND%20status%20%3D%20"2.%20Comparative%20Check%20%26%20Fixes"%20AND%20resolution%20%3D%20Unresolved%20AND%20"Auto%20Migration%20Status"%20%3D%20Success%20AND%20assignee%20in%20(atia.kabir%2C%20david.roker%2C%20EMPTY%2C%20oliver.bennett)%20AND%20"Peer%20Reviewer"%20in%20(EMPTY)%20ORDER%20BY%20priority%20DESC'
#Nikhil
# query = 'jql=project%20%3D%20CSM%20AND%20issuetype%20%3D%20Subject%20AND%20status%20in%20("1.%20Selected%20for%20Action"%2C%20Backlog)%20AND%20"Auto%20Migration%20Status"%20%3D%20Success%20AND%20Faculty%20in%20("Business%20and%20Economics"%2C%20Education%2C%20Engineering%2C%20"Melbourne%20Graduate%20School%20of%20Education"%2C%20Science)%20AND%20assignee%20in%20(EMPTY)%20ORDER%20BY%20status%20DESC%2C%20updated%20DESC'
#AUTH
import base64
cred =  "Basic " + base64.b64encode(b'oliver.bennett@unimelb.edu.au:h0tD9Rl1Ep4TTmnjHrWB8521').decode("utf-8")
headers = {
   "Accept": "application/json",
   "Content-Type": "application/json",
   "Authorization": cred
}
time.sleep(2)
#The first parameter of each request is your JQL search
canvas_response = requests.get('https://uomouajv.atlassian.net/rest/api/3/search?'+query+'&fields=customfield_12231', headers=headers)
bb_response = requests.get('https://uomouajv.atlassian.net/rest/api/3/search?'+query+'&fields=customfield_12266', headers=headers)

canvas_shell_list = []
bb_shell_list = []

#Build lists of source IDs
canvas_json = canvas_response.json()

for issue in canvas_json['issues']:
    for field in issue['fields']:
        canvas_shell_list.append(issue['fields'][field])

bb_json = bb_response.json()

for issue in bb_json['issues']:
    for field in issue['fields']:
        bb_shell_list.append(issue['fields'][field])

actionable_canvas = str(len(canvas_shell_list))
actionable_bb = str(len(bb_shell_list))
print('actionable_canvas: ' + actionable_canvas)
print('actionable_bb: ' + actionable_bb)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

password = 'margaretthatcheris110%SEXY'
email = 'oliver.bennett@unimelb.edu.au'
user_id = 'oliverb2'

users = ['atiak', 'droker','oliverb2','senhaoz1', 'mckew', 'akinyokuno', 'naranetaalan', 'hitoa', 'duricg', 'smitss', 'drummondk']

enrolee_id = users[10]
number_of_shells=4

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized") 
maximize = webdriver.ChromeOptions()
maximize.add_argument('--start-maximized')

print('Adding ' + str(enrolee_id) + ' to ' + str(number_of_shells) + ' shells...')
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

auth_user.send_keys(user_id)
auth_password.send_keys(password)
auth_password.send_keys(Keys.RETURN)
time.sleep(2)

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
for x in canvas_shell_list[:number_of_shells]:
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

#BLACKBOARD ENROLMENT LOOP

for x in bb_shell_list[:number_of_shells]:
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
        courseInfoSearchOperatorString = Select(blackboard.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[2]/div/form/fieldset/div[1]/select[2]'))
        courseInfoSearchOperatorString.select_by_visible_text('Equal to')
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
        element= WebDriverWait(blackboard, 10).until(
        EC.presence_of_element_located((By.ID, "quickEnrollLink")) #expected condition wait until the QuickEnrol button renders
        )
        quickEnrolButton = blackboard.find_element_by_id('quickEnrollLink')
        try:
            blackboard.find_element_by_class_name("enrolled")
            print('Enrolled class found. Admin is already enrolled.')
        except:
            print('enrolled Class not found. Admin needs to hit QuickEnrol Button')
            quickEnrolButton.click()
            
            alert = blackboard.switch_to_alert()
            alert.accept()
            print("Enrol as Coordinator BB alert accepted")      
    #JUMP HERE IF YOU'RE ALREADY ENROLLED
    try:
        element= WebDriverWait(blackboard, 10).until(
            EC.presence_of_element_located((By.ID, 'anonymous_element_16'))
        )
    except:
        print("can't find the CPanel")
    finally:
        blackboard.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        blackboard.find_element_by_link_text('Users and Groups').click()
        time.sleep(1)
         
    try:
        blackboard.find_element_by_link_text('Staff Roles').click()
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
        operator = Select(blackboard.find_element_by_id('operator'))
        operator.select_by_visible_text('Equal to')
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
        try:
            chevron.click()
            time.sleep(1)
            sc_target = blackboard.find_element_by_link_text('Subject coordinator')
            sc_target.click()
            # chevron.send_keys(Keys.ARROW_DOWN, Keys.RETURN)
            time.sleep(5)
        except:
            print('Failed to add user as SC.')
        element= WebDriverWait(blackboard, 10).until(
            EC.presence_of_element_located((By.ID, 'Sys Admin'))
        )
        blackboard.find_element_by_css_selector('#Sys\ Admin > a:nth-child(1)').click()
        #END BB ENROLMENT LOOPS
print('Successfully added ' + str(enrolee_id) + ' to ' + str(number_of_shells) + ' shells...')
