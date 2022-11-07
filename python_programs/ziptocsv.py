from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from pathlib import Path
import os
import zipfile
import csv
import xmltodict
from selenium.webdriver.chrome.options import Options
options = Options()  
options.add_argument("--headless") 
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
downloads_path = str(Path.home() / "Downloads")
chrome_prefs = {"download.default_directory":downloads_path} 
options.experimental_options["prefs"] = chrome_prefs
s = Service(executable_path='/usr/bin/chromedriver')
driver = webdriver.Chrome(service=s,options=options)
url='https://ftp.duvalclerk.com/'
driver.get(url)
driver.implicitly_wait(2)
driver.find_element(By.CSS_SELECTOR,'#user-box-text').send_keys('username')
driver.find_element(By.CSS_SELECTOR,'#pword-box-text').send_keys('password')
driver.find_element(By.CSS_SELECTOR,'#btn-LoginButton').click()
action=ActionChains(driver)
filename=driver.find_element(By.CSS_SELECTOR,'#ListFiles-row-0')
action.double_click(filename).perform()
time.sleep(2)
file_location=driver.find_element(By.XPATH,"/html[1]/body[1]/div[55]/div[5]/span[1]/span[1]/span[1]/span[2]/span[1]/span[1]/span[2]/span[1]/span[last()-1]")
action.double_click(file_location).perform()
a=[]
a.append(file_location.text.split('.'))
filename=a[0][0]
time.sleep(2)
zip_path=os.path.join(downloads_path,filename+'.zip')
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(downloads_path)
xml_path=os.path.join(downloads_path,filename+'.xml')
with open(xml_path, 'r') as xmlfile:
    xmlfiledata = xmlfile.read()
xmlfiledata_dict = xmltodict.parse(xmlfiledata)
petitionar_casedatas = [dict(x) for x in xmlfiledata_dict["Cases"]["Case"]]
HEADERS = ['CaseID', 'Department', 'DivisionName', 'CaseTypeDescription', 'CaseNumber', 'FileDate']
filerows = []
for petitionar_casedata in petitionar_casedatas:
    CaseID = petitionar_casedata["CaseID"]
    Department= petitionar_casedata["Department"]
    DivisionName= petitionar_casedata["DivisionName"]
    CaseTypeDescription = petitionar_casedata["CaseTypeDescription"]
    CaseNumber= petitionar_casedata["CaseNumber"]
    FileDate= petitionar_casedata["FileDate"]
    filerows.append([CaseID,Department,DivisionName,CaseTypeDescription,CaseNumber,FileDate])
csvfile_path=os.path.join(downloads_path,filename+'.csv')
with open(csvfile_path, 'w',newline="") as csvfile_write:
    write = csv.writer(csvfile_write)
    write.writerow(HEADERS)
    write.writerows(filerows)
case_Details=[*csv.DictReader(open(csvfile_path))]
for case_Detail in case_Details:
    case_Type=case_Detail['CaseTypeDescription']
    if 'EVICTION/DISTRESS FOR RENT' in case_Type:
       case_Number=case_Detail['CaseNumber']
       file_date_time=case_Detail['FileDate'].split('T')
       file_Date=file_date_time[0]
       print(case_Number)
       print(file_date_time)
       print(file_Date)
    elif 'Foreclosure' in case_Type:
        case_Number=case_Detail['CaseNumber']
        file_date_time=case_Detail['FileDate'].split('T')
        file_Date=file_date_time[0]
        print(case_Number) 
        print(file_date_time)
        print(file_Date) 