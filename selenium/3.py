#locate elements by their HTML ID attribute
from selenium import webdriver
driver= webdriver.Chrome()
driver.get("file:///C:/Users/ocben/pythonAutomation/page.html")
login_form = driver.find_element_by_id('loginForm')
print("My login form element is:")
print(login_form)
driver.close()
