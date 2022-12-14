
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import json


LOGIN = 'ivanivanov_test_hw@mail.ru'
PASSWORD = 'passwordfortest'

client = MongoClient('127.0.0.1', 27017)
db = client['db_mail']
mail_ru = db.mail_ru

service = Service('./chromedriver')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(15)
driver.maximize_window()
driver.get('https://account.mail.ru/')
action = ActionChains(driver)

login = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.NAME, 'username')))
login.send_keys(LOGIN)
login.send_keys(Keys.ENTER)

password = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.NAME, 'password')))
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

links, check = [], None
try:
    while True:
        dom = driver.find_elements(By.XPATH, "//span[@class='ll-crpt']/ancestor::a")
        if dom[-1] == check:
            break
        for link in dom:
            if link:
                elem = link.get_attribute('href')
                if elem not in links:
                    links.append(elem)
        check = dom[-1]
        action.move_to_element(check)
        action.perform()
        sleep(3)
except Exception as e:
    print(f'Error: {e}')

letter_info = {}
for link in links:
    driver.get(link)
    letter_info = {
        'sender': driver.find_element(By.XPATH, "//div[@class='letter__author']/span").text,
        'email_sender': driver.find_element(By.XPATH, "//div[@class='letter__author']/span").get_attribute('title'),
        'email_date': driver.find_element(By.XPATH, "//div[@class='letter__author']/div").text,
        'email_title': driver.find_element(By.TAG_NAME, 'h2').text,
        'link': link}
    try:
        mail_ru.insert_one(letter_info)
    except DuplicateKeyError:
        print(f'Letter {link} already exists')

