#adds all items to the cart
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

url = 'http://automationpractice.com/index.php?id_category=3&controller=category'
driver.get(url)

product_containers = driver.find_elements_by_class_name('product-container')

for index,product_container in enumerate(product_containers):
    hover = ActionChains(driver).move_to_element(product_container)
    hover.perform()
    #click on add to cart
    driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[%s]/div/div[2]/div[2]/a[1]/span'%(index+1)).click() #selenium uses non-zero index
    time.sleep(1) #wait for modal
    #click on continue shopping
    driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span').click()
    time.sleep(1)
