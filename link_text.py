from selenium import webdriver
import time

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)

"""driver.get("https://www.udemy.com/")
time.sleep(3)
driver.find_element("link text", "Sign up").click()
time.sleep(3)
driver.find_element("name", "full-name").send_keys("example123")
time.sleep(3)
driver.find_element("name", "email").send_keys("example1@gmail.com")
time.sleep(3)
driver.find_element("class name", "ud-btn.ud-btn-large.ud-btn-brand.ud-btn-text-md.passwordless-auth-mx-code-generation-form--submit-button--2vOvZ").click()"""


"""driver.get("https://www.selenium.dev/downloads/")
time.sleep(3)
driver.find_element("partial link text", "languages").click()"""


"""driver.get("https://demowebshop.tricentis.com/login")
time.sleep(3)
driver.find_element("css selector", "input[class='email']").send_keys("amitabhbachan@gmail.com")"""

# WAP to search something in amazon.in
"""driver.get("https://www.amazon.in/")
time.sleep(3)
driver.find_element("xpath","//input[@id='twotabsearchtextbox']").send_keys("shoes")
driver.find_element("xpath","//input[@id='nav-search-submit-button']").click()"""

"""driver.get("https://demowebshop.tricentis.com/login")
time.sleep(3)
driver.find_element("xpath","//a[@href='/register']").click()
time.sleep(3)
driver.find_element("xpath", "//input[@id='gender-female']").click()
time.sleep(3)
driver.find_element("xpath", "//input[@id='FirstName']").send_keys("mickey")
time.sleep(3)
driver.find_element("xpath", "//input[@id='LastName']").send_keys("mouse")
time.sleep(3)
driver.find_element("xpath", "//input[@id='Email']").send_keys("mickey.mousehaha12456@gmail.com")
time.sleep(3)
driver.find_element("xpath", "//input[@id='Password']").send_keys("mickeymouse123")
time.sleep(3)
driver.find_element("xpath", "//input[@id='ConfirmPassword']").send_keys("mickeymouse123")
time.sleep(3)
driver.find_element("xpath", "//input[@id='register-button']").click()
time.sleep(3)
driver.find_element("xpath", "//input[@class='button-1 register-continue-button']").click()
time.sleep(3)
driver.find_element("xpath","//a[@class='ico-logout']").click()
time.sleep(3)
driver.find_element("xpath", "//a[@href='/login']").click()
time.sleep(3)
driver.find_element("xpath", "//input[@id='Email']").send_keys("mickey.mousehaha12456@gmail.com")
time.sleep(3)
driver.find_element("xpath", "//input[@id='Password']").send_keys("mickeymouse123")
time.sleep(3)
driver.find_element("xpath","//input[@value='Log in']").click()
time.sleep(3)
driver.find_element("xpath", "//a[@href='/logout']").click()"""

"""driver.get("https://www.amazon.in/")
time.sleep(3)
driver.find_element("xpath", '''//a[text()="Today's Deals"]''').click()
time.sleep(3)
driver.find_element("xpath", "//button[text()='Coupons']").click()
time.sleep(3)
driver.find_element("xpath", "//span[text()='Appliances']").click()
time.sleep(3)"""

"""driver.get("https://blinkit.com/")
time.sleep(3)
driver.find_element("xpath", "//button[text()='Detect my location']").click()
time.sleep(3)
driver.find_element("xpath", "//div[text()='Login']").click()
time.sleep(3)"""

"""driver.get("https://www.facebook.com/r.php?entry_point=login")
time.sleep(3)
driver.find_element("xpath", "(//input[@type='text'])[1]").send_keys("Ram")
time.sleep(3)
driver.find_element("xpath", "(//input[@type='text'])[2]").send_keys("Kumar")
time.sleep(3)
driver.find_element("xpath", "(//input[@type='text'])[5]").send_keys("Ram@gmail.com")
time.sleep(3)"""

"""driver.get("https://www.giva.co/")
time.sleep(3)
driver.find_element("xpath", "//span[contains(text(),'Gold with Lab Diamonds']").click()
time.sleep(3)
driver.find_element("xpath", "//span[contains(text(),'GIVA Gift Card']").click()
time.sleep(3)"""

"""driver.get("https://www.python.org/downloads/")
time.sleep(3)
driver.find_element("xpath", "//a[text()='Python 3.12.12']/../..//a[text()='Release Notes']").click()
time.sleep(3)"""

driver.get("https://in.tradingview.com/")
time.sleep(3)
driver.find_element("xpath",'//span[text()="Search"]').click()
time.sleep(3)
driver.find_element("xpath", "//input[@name='query']").send_keys("HAL")
time.sleep(3)
driver.find_element("xpath", "aria-hidden="true"").click()
time.sleep(3)
driver.find_element("xpath", "(//button[@aria-label='Search'])[3]").click()
time.sleep(3)






