import time
from selenium import webdriver
from selenium.webdriver import Keys

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)

# driver.get("https://www.instagram.com/")
# time.sleep(2)
# driver.find_element('name','username').send_keys('nandini')
# time.sleep(2)
# driver.find_element('name','password').send_keys('nandini@12345')
# time.sleep(2)

# driver.get("https://www.facebook.com/r.php?entry_point=login")
# time.sleep(2)
# driver.find_element('name','firstname').send_keys('nandini')
# time.sleep(2)
# driver.find_element('name','lastname').send_keys('gs')
# time.sleep(2)
# driver.find_element('name','reg_email__').send_keys('nandini.gmail.com')
# time.sleep(2)
# driver.find_element('id','password_step_input').send_keys('nandini@12345')
# time.sleep(2)

# driver.get("https://demowebshop.tricentis.com/register ")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element("class name", "text-box.single-line").send_keys("selenium")

"""driver.get("https://demowebshop.tricentis.com ")
driver.maximize_window()
time.sleep(2)
driver.find_element("tag name", "a").click()

driver.get("https://demowebshop.tricentis.com/register ")
time.sleep(2)
driver.find_element("tag name", "input").send_keys("Selenium")"""




