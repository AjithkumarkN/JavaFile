#from FtpFileDownload import *
from ConvertXmlToCsv import *
#from selenium.webdriver.common.by import By
from datetime import date
#import os
#import csv
from selenium.common.exceptions import NoSuchElementException
class TenantAndLispendens():
    driver=FtpFileDownlod.driver
    court_url='https://core.duvalclerk.com/CoreCms.aspx'
    driver.get(court_url)
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR,"input[name='ctl00$c_UsernameTextBox']").send_keys('dual clerk username')
    driver.find_element(By.CSS_SELECTOR,"input[name='ctl00$c_PasswordTextBox']").send_keys('dual clerk password')
    driver.find_element(By.CSS_SELECTOR,"input[value='Login to CORE']").click()  
    today_dateTime = date.today()
    today_Date = today_dateTime.strftime("%Y-%m-%d")
    download_path=FtpFileDownlod.download_path
    filename=FtpFileDownlod.filename
    convert_tenantfile=os.path.join(download_path,'tenent-'+today_Date+'.csv')
    convert_lispendensefile=os.path.join(download_path,'lispendence-'+today_Date+'.csv')
    tenant_casedetails=[]
    lispendense_casedetails=[]  
    def get_casenumber(self):
        csvfile_path=ConvertXmlToCsv.csvfile_path
        csvfile_path=os.path.join(self.download_path,self.filename+'.csv')
        case_Details=[*csv.DictReader(open(csvfile_path))]
        for case_Detail in case_Details:
            case_Type=case_Detail['CaseTypeDescription'].upper()
            if 'EVICTION/DISTRESS FOR RENT' in case_Type:
                case_Number=case_Detail['CaseNumber']
                file_date_time=case_Detail['FileDate'].split('T')
                file_Date=file_date_time[0]
                obj.tenant_lispendens_searchCaseStatus(case_Number,file_Date,case_Type)
            elif 'FORECLOSURE' in case_Type:
                case_Number=case_Detail['CaseNumber']
                file_date_time=case_Detail['FileDate'].split('T')
                file_Date=file_date_time[0]
                obj.tenant_lispendens_searchCaseStatus(case_Number,file_Date,case_Type)
        #obj.write_csvfile() 
        os.remove(csvfile_path)
    def tenant_lispendens_searchCaseStatus(self,case_Number,file_Date,case_Type):
        try:
            self.driver.find_element(By.CSS_SELECTOR,'body > form:nth-child(1) > div:nth-child(35) > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) \
            > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > input:nth-child(1)').send_keys(case_Number)
            self.driver.find_element(By.CSS_SELECTOR,'body > form:nth-child(1) > div:nth-child(35) > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) \
            > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > input:nth-child(1)').click()
            case_Id = self.driver.find_element(By.XPATH,("//span[@id='c_CaseNumberLabel']")).text
            case_Status = self.driver.find_element(By.XPATH,("//div[@class='caseDisplayTable caseSummary']/table/tbody/tr[2]/td[2]")).text
            if 'EVICTION/DISTRESS FOR RENT' in case_Type:
                if(file_Date==self.today_Date):    
                    if (case_Status=='OPEN'):
                            petitioner_Name = self.driver.find_element(By.XPATH,("//div[@class='caseDisplayTable']/table/tbody[2]/tr/td[1]")).text
                            party_type = self.driver.find_element(By.XPATH,("//div[@class='caseDisplayTable']/table/tbody[2]/tr/td[2]")).text
                            petitioner_Address = self.driver.find_element(By.XPATH,("//div[@class='caseDisplayTable']/table/tbody[2]/tr/td[3]")).text
                            tenant_CaseDetail= [
                                            {'Case_ID': case_Id, 'Case_Status': case_Status, 'Petitioner_Name': petitioner_Name, 'Party_Type':party_type, 'Address':petitioner_Address},
                                            ]
                            self.tenant_casedetails+=tenant_CaseDetail
                            self.driver.refresh()   
                    else:    
                        self.driver.refresh() 
                elif(case_Status=='OPEN'):
                    tenant_casestatus = [
                            {'Case_ID': case_Id, 'Case_Status': case_Status}, 
                                ]
                    self.tenant_casedetails+=tenant_casestatus
                    self.driver.refresh()
                else:
                    self.driver.refresh()        
            elif 'FORECLOSURE' in case_Type:        
                if (case_Status=='OPEN'):
                    lispendense_casestatus = [
                            {'Case_ID': case_Id, 'Case_Status': case_Status}, 
                                ]
                    self.lispendense_casedetails+=lispendense_casestatus
                    self.driver.refresh()
                else:
                    self.driver.refresh()  
        except NoSuchElementException:
            self.driver.refresh()
    '''def write_csvfile(self):
        convert_tenantfile=os.path.join(self.download_path,'tenent-'+self.today_Date+'.csv')
        convert_lispendensefile=os.path.join(self.download_path,'lispendence-'+self.today_Date+'.csv')
        csv_Headings=['Case_ID','Case_Status','Petitioner_Name','Party_Type','Address']
        with open(convert_tenantfile, 'w', newline='') as tenant_outputfile:
            tenant_dict_writer = csv.DictWriter(tenant_outputfile, fieldnames=csv_Headings)
            tenant_dict_writer.writeheader()
            tenant_dict_writer.writerows(self.tenant_casedtails)
        with open(convert_lispendensefile, 'w', newline='') as lispendense_outputfile:
            lispendense_dict_writer = csv.DictWriter(lispendense_outputfile, fieldnames=csv_Headings)
            lispendense_dict_writer.writeheader()
            lispendense_dict_writer.writerows(self.lispendense_casedetails)'''
obj=TenantAndLispendens()
obj.get_casenumber()
