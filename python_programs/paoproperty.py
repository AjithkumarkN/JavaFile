from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import pandas as pd
import csv
#options = Options()  
#options.add_argument("--headless") 
s = Service(executable_path='/usr/bin/chromedriver')
driver = webdriver.Chrome(service=s)
url='https://paopropertysearch.coj.net/Basic/Search.aspx'
driver.get(url)
driver.implicitly_wait(1)
current_location_opath=os.path.dirname(os.path.abspath(__file__))
pao_csvfile_path=os.path.join(current_location_opath,'paofiles',"PAO - Sheet1.csv")
pao_Details=[*csv.DictReader(open(pao_csvfile_path))]
try:
    property_Details=[]
    for pao_Detail in pao_Details:
        primary_address=pao_Detail['Primary Residence'].split(" ")
        street_number=primary_address[0]
        #street_name=primary_address[2]
        zipcode=pao_Detail['PrimaryResidenceZip']
        driver.find_element(By.CSS_SELECTOR,"#ctl00_cphBody_tbStreetNumber").send_keys(street_number)
        #driver.find_element(By.CSS_SELECTOR,"#ctl00_cphBody_tbStreetName").send_keys(street_name)
        driver.find_element(By.CSS_SELECTOR,"#ctl00_cphBody_tbZipCode").send_keys(zipcode)
        driver.find_element(By.CSS_SELECTOR,"#ctl00_cphBody_bSearch").click()
        Re=driver.find_element(By.CSS_SELECTOR,"#ctl00_cphBody_gridResults > tbody > tr:nth-child(2) > td:nth-child(1)").text
        Name=driver.find_element(By.CSS_SELECTOR,"#ctl00_cphBody_gridResults > tbody > tr:nth-child(2) > td:nth-child(2)").text
        Street=driver.find_element(By.CSS_SELECTOR,"#ctl00_cphBody_gridResults > tbody > tr:nth-child(2) > td:nth-child(3)").text
        Street_name=driver.find_element(By.CSS_SELECTOR,"#ctl00_cphBody_gridResults > tbody > tr:nth-child(2) > td:nth-child(4)").text
        Type=driver.find_element(By.CSS_SELECTOR,"#ctl00_cphBody_gridResults > tbody > tr:nth-child(2) > td:nth-child(5)").text
        Direction=driver.find_element(By.CSS_SELECTOR,"#ctl00_cphBody_gridResults > tbody > tr:nth-child(2) > td:nth-child(6)").text
        Unit=driver.find_element(By.CSS_SELECTOR,"#ctl00_cphBody_gridResults > tbody > tr:nth-child(2) > td:nth-child(7)").text
        City=driver.find_element(By.CSS_SELECTOR,"#ctl00_cphBody_gridResults > tbody > tr:nth-child(2) > td:nth-child(8)").text
        Zip=driver.find_element(By.CSS_SELECTOR,"#ctl00_cphBody_gridResults > tbody > tr:nth-child(2) > td:nth-child(9)").text
        property_Detail=[
            {'RE':Re,'NAME':Name,'STREET':Street,'STREET NAME':Street_name,'TYPE':Type,'DIRECTION':Direction,'UNIT':Unit,'CITY':City,'ZIP':Zip}
        ]
        property_Details+=property_Detail
        csv_Headings=property_Details[0].keys()
        print(property_Details)
        New_search=driver.find_element(By.CSS_SELECTOR,"#ctl00_cphBody_lbNewSearch").click()
except NoSuchElementException:
    New_search=driver.find_element(By.CSS_SELECTOR,"#ctl00_cphBody_lbNewSearch").click()
with open(f'{pao_csvfile_path}convertfile.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, csv_Headings)
    dict_writer.writeheader()
    dict_writer.writerows(property_Details)            

    




