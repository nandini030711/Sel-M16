#11\12\2025
#Dynamically changing values

from selenium import webdriver
import time

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)

driver.get("https://www.iforex.in/tools/live-rates")
time.sleep(2)

driver.find_element("xpath", "(//div[@id='ai-chat-bubble-close'])[2]").click()
time.sleep(4)

gold_sell_price = driver.find_element("xpath","(//div[text()='Gold']/../..//span)[2]")
gold_buy_price = driver.find_element("xpath","(//div[text()='Gold']/../..//span)[3]")

#print(gold_sell_price)
#print(gold_buy_price) If we print just the webelement then it will give the address of the web element. So we have to use the text attribute to get the value of the webelement

print(f"The sell price of gold is {gold_sell_price.text}")
print(f"The buy price of gold is {gold_buy_price.text}")





