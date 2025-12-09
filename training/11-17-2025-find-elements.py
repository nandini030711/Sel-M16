#WAP to get all the links in the www.python.org link


import time

from selenium import webdriver


driver = webdriver.Firefox()

driver.get("https://www.python.org/")
time.sleep(2)

'''All the links --> href --> <a>'''

all_links = driver.find_elements('tag name', 'a')   ##List of web elements  ##[a1,a2,a3,a4,a5] here the locator we are using is tag name

for link in all_links:
    print(link.get_attribute('href'))    ##get_attribute property is used to get the attribute value

##########################################################################################################################################################################
import time

from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
