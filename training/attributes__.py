from selenium import webdriver
import time
from selenium import webdriver
import time

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)

driver.get("https://www.myntra.com")
time.sleep(2)

