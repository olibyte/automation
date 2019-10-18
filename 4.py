#locate elements by their HTML ID attribute
from selenium import webdriver
driver= webdriver.Chrome()
driver.get("file:///C:/Users/ocben/pythonAutomation/page.html")
username = driver.find_element_by_name('username')
print("My input element is:")
print(username)
driver.close()
