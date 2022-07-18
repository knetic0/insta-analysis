from main import targetName, userName, password
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait

import os, sys

# Logging and Scraping is here. 


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("headless")

driver = webdriver.Chrome(executable_path = r"chromedriver")
url = "https://www.instagram.com/?hl=tr"

driver.get(url)

time.sleep(5)

print("[+] Logging in....")

# login to instagram here.

loginUserName = driver.find_element_by_name("username")
loginUserName.send_keys(userName)


loginPassword = driver.find_element_by_name("password")
loginPassword.send_keys(password)

loginButton = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button")
loginButton.click()

time.sleep(10)

print("[+] Login Successful!")

time.sleep(2)

print("[+] Loading....")

#----------------------------

# not now buttons

notnow = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
notnow.click()

time.sleep(15)

notnow_2 = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
notnow_2.click()

# -------------------   

time.sleep(10)

# search target

current_URL = f"https://www.instagram.com/{targetName}/"

driver.get(current_URL)

print("[+] Forwarding Successful!")


#-------------------

print("[+] Scraping Datas....")

time.sleep(10)

# scraping datas

all_datas = driver.find_elements_by_class_name("_ac2a")

posts = all_datas[0].text
followers = all_datas[1].text
following = all_datas[2].text

print("[+] Importing Datas...")

time.sleep(5)

import datas

print("[+] Successful!")

#----------------