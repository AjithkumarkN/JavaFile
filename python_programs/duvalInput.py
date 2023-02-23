from fileinput import filename
from importlib.resources import path
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import date
import os
import csv


class tenantLis():
    options = Options()  
    options.add_argument("--headless") 
    s = Service(executable_path='/media/funbook/74622996-999c-45ee-b9ae-bc3cde298dc4/funbook/chrome-driver/chromedriver')
    driver = webdriver.Chrome(service=s,options=options)
    url='https://core.duvalclerk.com/CoreCms.aspx'
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR,"input[name='ctl00$c_UsernameTextBox']").send_keys('username')
    driver.find_element(By.CSS_SELECTOR,"input[name='ctl00$c_PasswordTextBox']").send_keys('password')
    driver.find_element(By.CSS_SELECTOR,"input[value='Login to CORE']").click()
    def checkCaseStatus(self,case_Id,case_Status,to_csv1):
        try:
            if (case_Status=='OPEN'):
                print(case_Status)
                to_csv = [
                        {'Case_ID': case_Id, 'Case_Status': case_Status,},

                            ]
                to_csv1+=to_csv                
                self.driver.refresh()
            else:
                self.driver.refresh() 
        except NoSuchElementException:
            self.driver.refresh()           
    def tenantLisSearch(self,caseDetails,tenant,fileName,today_FileDate,lispendens):
        try:
            to_csv1=[]
            for i in caseDetails:
                casenumber=i['CaseNumber']
                filedateAndtime=i['FileDate'].split(' ')
                filedate=filedateAndtime[0]
                self.driver.find_element(By.CSS_SELECTOR,'body > form:nth-child(1) > div:nth-child(35) > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) \
                > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > input:nth-child(1)').send_keys(casenumber)
                self.driver.find_element(By.CSS_SELECTOR,'body > form:nth-child(1) > div:nth-child(35) > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) \
                > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > input:nth-child(1)').click()
                case_Id = self.driver.find_element(By.XPATH,("//span[@id='c_CaseNumberLabel']")).text
                print(case_Id)
                case_Status = self.driver.find_element(By.XPATH,("//div[@class='caseDisplayTable caseSummary']/table/tbody/tr[2]/td[2]")).text
                print(case_Status)
                if(fileName==tenant):
                    if(filedate==today_FileDate):    
                        if (case_Status=='OPEN'):
                                petitioner_Name = self.driver.find_element(By.XPATH,("//div[@class='caseDisplayTable']/table/tbody[2]/tr/td[1]")).text
                                party_type = self.driver.find_element(By.XPATH,("//div[@class='caseDisplayTable']/table/tbody[2]/tr/td[2]")).text
                                petitioner_Address = self.driver.find_element(By.XPATH,("//div[@class='caseDisplayTable']/table/tbody[2]/tr/td[3]")).text
                                to_csv= [
                                                {'Case_ID': case_Id, 'Case_Status': case_Status, 'Petitioner_Name': petitioner_Name, 'Party_Type':party_type, 'Address':petitioner_Address},
                                                ]
                                to_csv1+=to_csv
                                self.driver.refresh()   
                        else:    
                            self.driver.refresh()
                        keys = to_csv[0].keys() 
                    elif(case_Status=='OPEN'):
                        obj.checkCaseStatus(case_Id,case_Status,to_csv1)
                        self.driver.refresh()
                    else:
                        self.driver.refresh()              
                elif(fileName==lispendens):            
                    if (case_Status=='OPEN'):
                        obj.checkCaseStatus(case_Id,case_Status,to_csv1)
                        self.driver.refresh()
                    else:
                        self.driver.refresh()
                    keys = to_csv1[0].keys()      
        except NoSuchElementException:
            self.driver.refresh()

        with open(f'{fileName}.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(to_csv1)            

user_fileName=input("which file you want use tenant or lispendens:")
today_dateTime = date.today()
today_Date = today_dateTime.strftime("%d-%m-%Y")
directory_path=os.path.dirname(os.path.abspath(__file__))
print(directory_path)
complete_path=os.path.join(directory_path,'{}-{}{}'.format(user_fileName,today_Date,'.csv'))
print(complete_path)
caseDetails=[*csv.DictReader(open(complete_path))]
fileName=os.path.basename(complete_path)
tenant="tenant-"+today_Date+".csv"
lispendens="lispendens-"+today_Date+".csv"
obj=tenantLis()
today_FileDate = today_dateTime.strftime("%m-%d-%Y")
obj.tenantLisSearch(caseDetails,tenant,fileName,today_FileDate,lispendens)
