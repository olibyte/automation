from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
source = driver.find_element_by_xpath('//*[@id="box3"]')
dest = driver.find_element_by_xpath('//*[@id="box103"]')
actions = ActionChains(driver)
actions.drag_and_drop(source, dest).perform()