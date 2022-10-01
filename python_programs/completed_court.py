from msilib.schema import Class, ODBCTranslator
from operator import index, indexOf
from re import I
from traceback import print_tb
from urllib import request
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.chrome.options import Options
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
 

df = pd.read_csv("D:\AK\Pdf_to_text\dual_court\Copy of lispendens of september - 01_09_2022.csv")
data=df.iloc[:,4:5].values
chrome_options = Options()  
chrome_options.add_argument("--headless") 
s = Service('D:\AK\ChromeDriver\chromedriver.exe')
driver = webdriver.Chrome(service=s,chrome_options=chrome_options)
url='https://core.duvalclerk.com/CoreCms.aspx'
driver.get(url)
driver.implicitly_wait(1)
driver.find_element(By.CSS_SELECTOR,"input[name='ctl00$c_UsernameTextBox']").send_keys('sean@ozellrealestate.com')
driver.find_element(By.CSS_SELECTOR,"input[name='ctl00$c_PasswordTextBox']").send_keys('RealEstate45!')

driver.find_element(By.CSS_SELECTOR,"input[value='Login to CORE']").click()
to_csv1=[]
for i in data:
        
    driver.find_element(By.CSS_SELECTOR,'body > form:nth-child(1) > div:nth-child(35) > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > input:nth-child(1)').send_keys(i)
    driver.find_element(By.CSS_SELECTOR,'body > form:nth-child(1) > div:nth-child(35) > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > input:nth-child(1)').click()
    try:
        table = driver.find_element(By.XPATH,("//span[@id='c_CaseNumberLabel']")).text
        print(table)
        table1 = driver.find_element(By.XPATH,("//div[@class='caseDisplayTable caseSummary']/table/tbody/tr[2]/td[2]")).text
        print(table1)
        if (table1=='OPEN'):
            table2 = driver.find_element(By.XPATH,("//div[@class='caseDisplayTable']/table/tbody[2]/tr/td[1]")).text
            table3 = driver.find_element(By.XPATH,("//div[@class='caseDisplayTable']/table/tbody[2]/tr/td[2]")).text
            table4 = driver.find_element(By.XPATH,("//div[@class='caseDisplayTable']/table/tbody[2]/tr/td[3]")).text
            to_csv = [
                    {'Caser_ID': table, 'Case_Status': table1, 'Petitioner_Name': table2, 'Party_Type':table3, 'Address':table4},
                    
                    ]
            to_csv1+=to_csv
            driver.refresh()
        else:
            driver.refresh()
    except NoSuchElementException:
        driver.refresh()
    
keys = to_csv[0].keys()
with open('D:\AK\Pdf_to_text\dual_court\people.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(to_csv1)
