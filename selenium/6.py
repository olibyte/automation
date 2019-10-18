#locate elements using class
from selenium import webdriver
driver= webdriver.Chrome()
driver.get("file:///C:/Users/ocben/pythonAutomation/page.html")


content = driver.find_element_by_class_name("content")
print("My class element is: ")
print(content)  

driver.close()
