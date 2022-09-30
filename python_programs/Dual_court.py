from msilib.schema import Class
from operator import index, indexOf
from re import I
from traceback import print_tb
from urllib import request
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup   
import requests 
import pandas as pd
from openpyxl import Workbook
import xlsxwriter
from selenium.webdriver.chrome.options import Options
 
google_sheetId="1NypSapo7XLamkby-wuDfmhP08Lc0G_TZEgP0i7G2ysA"
sheet_name="Datavalue"

gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(google_sheetId, sheet_name)
print(gsheet_url)
df = pd.read_csv(gsheet_url)
data=df.iloc[:,4:5].values
chrome_options = Options()  
chrome_options.headless=True #add_argument("--headless") 
s = Service('D:\AK\ChromeDriver\chromedriver.exe')
driver = webdriver.Chrome(service=s,chrome_options=chrome_options)
url='https://core.duvalclerk.com/CoreCms.aspx'
driver.get(url)

driver.find_element('xpath','//*[@id="c_UsernameTextBox"]').send_keys('sean@ozellrealestate.com')
driver.find_element('xpath','//*[@id="c_PasswordTextBox"]').send_keys('RealEstate45!')
time.sleep(1)
driver.find_element('xpath','//*[@id="LoginDialog"]/tbody/tr[4]/td[2]/input').click()
for i in data:
   
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,'body > form:nth-child(1) > div:nth-child(35) > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > input:nth-child(1)').send_keys(i)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,'body > form:nth-child(1) > div:nth-child(35) > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > input:nth-child(1)').click()
    time.sleep(7)
    table = driver.find_element(By.XPATH,("//span[@id='c_CaseNumberLabel']")).text
    print(table)
    table1 = driver.find_element(By.XPATH,("//div[@class='caseDisplayTable caseSummary']/table/tbody/tr[2]/td[1]")).text
    table2 = driver.find_element(By.XPATH,("//div[@class='caseDisplayTable caseSummary']/table/tbody/tr[2]/td[2]")).text
    print(table2)
    if (table2=='OPEN'):
        table3 = driver.find_element(By.XPATH,("//div[@class='caseDisplayTable']/table/tbody[2]/tr/td[1]")).text
        table4 = driver.find_element(By.XPATH,("//div[@class='caseDisplayTable']/table/tbody[2]/tr/td[2]")).text
        table5 = driver.find_element(By.XPATH,("//div[@class='caseDisplayTable']/table/tbody[2]/tr/td[3]")).text
        print("{},{},{},{},{},{}\n".format(table,table1,table2,table3,table4.strip().replace("\n"," "),table5.replace("\n", " ")))
        file=open("D:\AK\Pdf_to_text\dual_court\Datas_file13.txt",'a')
        print(file.write("{},{},{},{},{},{}\n".format(table,table1,table2,table3,table4.strip().replace("\n"," "),table5.replace("\n", " "))))
        driver.refresh()
    else:
        driver.refresh()
time.sleep(2)        
read_file = pd.read_csv ('D:\AK\Pdf_to_text\dual_court\Datas_file13.txt')
time.sleep(5)
read_file.to_csv ('D:\AK\Pdf_to_text\dual_court\Datas_file13.csv',index=None)      

