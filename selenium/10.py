#performs a search for text 'Beginner'
#in the left-side menu bar, changes value from More Options to Raw Text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get('https://wiki.python.org/moin/FrontPage')

searchBox= driver.find_element_by_id('searchinput')
searchBox.clear()
searchBox.send_keys("Beginner")
searchBox.send_keys(Keys.RETURN)
time.sleep(5)

#no unique identifier, so last resort is to find by xpath.
select = Select(driver.find_element_by_xpath('//*[@id="sidebar"]/div[3]/ul/li[5]/form/div/select'))

#guessing the relative path: at least 2 levels, a few intermediate levels and a form and div.
#select = Select(driver.find_element_by_xpath('//*/form/div/select'))
select.select_by_visible_text("Raw Text")
time.sleep(5)

driver.close()