import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#we are importing the ActionChains class from the action_chains module

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)

ac_obj = ActionChains(driver)

driver.get("https://www.kushals.com/")
time.sleep(2)

driver.find_element()
