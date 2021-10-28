#including necessary libraries
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#launching firefox
driver=webdriver.Firefox()
driver.get("https://play.typeracer.com")
time.sleep(2)
driver.find_element_by_link_text('Enter a Typing Race').click()
#this is for the time i have to wait while the match starts
time.sleep(20)
#copying the text
thisisit=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div')
#that annoying popup which teaches you how to play
driver.find_element_by_css_selector('.xButton').click()
time.sleep(0.5)
for i in thisisit.text:
    #you can adjust the speed by yourself if you want but when we exceed 100wpm it gives another popup where we are needed to write another test which sounded boring so i didn't write anything for it
    time.sleep(.1)
    #gives nearly 90wpm (10 characters per second)
    driver.find_element_by_css_selector('.txtInput').send_keys(i)
#to be able to watch your results
time.sleep(10)
for i in range (2):
    #i wanted it not to just write a single time but as many times as we wish.
    driver.find_element_by_css_selector('.raceAgainLink').click()
    time.sleep(15)
    thisisit=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div')
    time.sleep(.5)
    #there will be another popup after two or three tests . i didn't write anything for it but i might add in future
    for i in thisisit.text:
        time.sleep(.1)
        driver.find_element_by_css_selector('.txtInput').send_keys(i)
    time.sleep(10)
