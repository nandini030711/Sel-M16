import time

from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
