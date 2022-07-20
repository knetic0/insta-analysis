from main import targetName, userName, password
from text import write
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import instaloader
from selenium.webdriver.support.ui import WebDriverWait

import os, sys

# Logging and Scraping is here. 

os.system("clear")

print(write)

time.sleep(2)

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("headless")

driver = webdriver.Chrome(executable_path = r"chromedriver")
url = "https://www.instagram.com/?hl=tr"

driver.get(url)

time.sleep(5)

print("[+] Logging in....")

# login to instagram here.

try:

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

    # posts, followers, following


    posts = all_datas[0].text
    followers = all_datas[1].text
    following = all_datas[2].text
    bio = driver.find_element_by_class_name("_aa_c").text

    new_url = f"https://www.instagram.com/{targetName}/followers"

    driver.get(new_url)

    # followers

    print("[+] Scraping Follower's...")

    time.sleep(10)

    instaloader_ = instaloader.Instaloader()
    instaloader_.login(userName, password)

    profile = instaloader.Profile.from_username(instaloader_.context, targetName)

    followers_nameList = []

    for follower_ in profile.get_followers():
        followers_nameList.append(follower_.username)

    follow_nameList = []

    for follow_ in profile.get_followees():
        follow_nameList.append(follow_.username)


    print("[+] Importing Datas...")

    time.sleep(5)

    import datas

    print("[+] Successful!")

    time.sleep(3)

    driver.close()

#----------------

except:

    print("[+] Error. Try Again...")
    driver.close()
