"""import time

from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)

driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)

footer_elements=driver.find_elements("xpath", "//div[@class='footer-menu-wrapper']//a") # find_elements will find multiple occurences
print(footer_elements) #This will print the addresses of the webelements in a list

for ele in footer_elements:
    print(ele.text) # since its a list, we have to put in loop and print the textwrap"""

##################################################################################################################################################################

import time

from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)

driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)

categories = driver.find_elements("xpath", "//div[@class='block block-category-navigation']//a")
print(categories)

for ele in categories:
    print(ele.text)

########################################################################################################################################################


import time

from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)

driver.get("https://www.myntra.com/")
time.sleep(2)

driver.find_element()



