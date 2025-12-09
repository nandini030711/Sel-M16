import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#we are importing the ActionChains class from the action_chains module

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)

ac_obj = ActionChains(driver)

# driver.get("https://www.myntra.com/")
# time.sleep(2)

# ac_obj.send_keys(Keys.END).perform()
# time.sleep(2)
#
# ac_obj.send_keys(Keys.HOME).perform()
# time.sleep(2)
#
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
#
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
#
# ac_obj.send_keys(Keys.PAGE_UP).perform()
# time.sleep(2)
#############################################################################################################################
'''Drag and drop'''

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

ele = driver.find_element("xpath", "//h2[text()='SVG Elements']")
ac_obj.scroll_to_element(ele).perform()
time.sleep(2)

# draggable_ele = driver.find_element("xpath", "//div[@id='draggable']")
# droppable_ele = driver.find_element("xpath", "//div[@id='droppable']")
#
# ac_obj.drag_and_drop(draggable_ele, droppable_ele).perform()
# time.sleep(2)

#############################################################################################################





