from msilib.schema import Class
from traceback import print_tb
from urllib import request
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup   
import requests 
import pandas as pd
from urllib.request import urlopen

s = Service('D:\AK\ChromeDriver\chromedriver.exe')
driver = webdriver.Chrome(service=s)
 
url='https://core.duvalclerk.com/CoreCms.aspx'
driver.get(url)

driver.find_element('xpath','//*[@id="c_UsernameTextBox"]').send_keys('sean@ozellrealestate.com')
driver.find_element('xpath','//*[@id="c_PasswordTextBox"]').send_keys('RealEstate45!')
time.sleep(2)
driver.find_element('xpath','//*[@id="LoginDialog"]/tbody/tr[4]/td[2]/input').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'body > form:nth-child(1) > div:nth-child(35) > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > input:nth-child(1)').send_keys('16-2022-DR-005902-FMXX-MA')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'body > form:nth-child(1) > div:nth-child(35) > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > input:nth-child(1)').click()

table=pd.read_html(url)
print(len(table))