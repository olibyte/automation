from selenium import webdriver
import time
from selenium.webdriver import ActionChains

#open maximized
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")

#create driver instance
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://jqueryui.com/droppable')
#switch to first frame to access drap and drop directly
driver.switch_to.frame(0)

#action_chains enables us to automate actions
#actions are queued and .perform(ed) as they're added to the queue
action_chains= ActionChains(driver)

source= driver.find_element_by_id('draggable')
target = driver.find_element_by_id('droppable')


action_chains.drag_and_drop_by_offset(source, 100, 100).perform()
time.sleep(2)

action_chains.drag_and_drop(source, target).perform()
time.sleep(2)

driver.close()
