"Upload single file"
import os

# import time
#
# from selenium import webdriver
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# #driver.find_element('xpath','//input[@id="singleFileInput"]').click() # This will throw an invalidArgumentException because clicking on the choose file button will direct to the local machine and selenium
#     #works only on web applications. Selenium gets confused to handle it and will throw exception. Selenium will not allow the click operation itself after identifying the locator
#     #That's why it throws invalidArgumentException and not no such element exception. So we have use send keys()
# #time.sleep(2)
#
# driver.find_element('xpath','//input[@id="singleFileInput"]').send_keys(r'C:\Users\nandi\PycharmProjects\Selenium_Training\files\myntra_homepage.png')
# time.sleep(2)

########################################################################################################################################################################3

"""Upload multiple files"""

# import time
#
# from selenium import webdriver
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# file1 = r"C:\Users\nandi\PycharmProjects\Selenium_Training\locators\_1_id.py"
# file2 = r"C:\Users\nandi\PycharmProjects\Selenium_Training\locators\_2_name.py"
# file3 = r"C:\Users\nandi\PycharmProjects\Selenium_Training\files\myntra_homepage.png"
#
# driver.find_element('xpath','//input[@id="multipleFilesInput"]').send_keys(f'{file1} \n {file2} \n {file3}') ## Send keys will only take one argument. So if we have to send multiple file names, we have to store it in different variables amd then pass it as one entity within ' ' preceded by format string f
# time.sleep(2)

#############################################################################################################################################################

"""Download files for chrome """

# import time
#
# from selenium import webdriver
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# prefs = {
#     "download.default_directory": r"C:\Users\nandi\PycharmProjects\Selenium_Training\files",
#     "download.prompt_for_download": False,
#     "safebrowsing.enabled": True,
#     "plugins.always_open_pdf_externally": True
# }
#
# opts.add_experimental_option("prefs", prefs)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://demoqa.com/upload-download")
# time.sleep(2)
#
# driver.find_element('xpath','//a[text()="Download"]').click()

######################################################################################################################################
"""Download files for firefox """
import time

from selenium import webdriver

opts=webdriver.FirefoxOptions()
opts.set_preference("browser.download.folderList",2)
opts.set_preference("browser.download.dir",r"C:\Users\nandi\PycharmProjects\Selenium_Training\files")
opts.set_preference("pdfjs.disabled", True)

driver=webdriver.Firefox(opts)

driver.get("https://demoqa.com/upload-download")
time.sleep(2)

driver.find_element('xpath','//a[text()="Download"]').click()


#################################################################################################################################


