import time
from wsgiref.util import application_uri

from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)

# #launch the application
driver.get("https://www.myntra.com")
time.sleep(2)
#
# #maximize the browser
# driver.maximize_window()
# time.sleep(2)
#
# #minimize the browser
# # driver.minimize_window()
# # time.sleep(2)
#
# #to go back
# driver.back()
# time.sleep(2)
#
# #to go forward
# driver.forward()
# time.sleep(2)
#
# #to refresh
# driver.refresh()
# time.sleep(2)

# print(driver.current_url)
# print(driver.title)
# print(driver.name)
# print(driver.page_source)

#to take the screenshot
driver.save_screenshot(r"C:\Users\nandi\PycharmProjects\Selenium_Training\files\myntra_homepage.png")


