from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException   
from datetime import date
import os
import csv
from flask import Flask,render_template,request,send_file


class tenant_And_Lispendens():
    options = Options()  
    options.add_argument("--headless") 
    s = Service(executable_path='/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=s,options=options)
    url='https://core.duvalclerk.com/CoreCms.aspx'
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR,"input[name='ctl00$c_UsernameTextBox']").send_keys('username')
    driver.find_element(By.CSS_SELECTOR,"input[name='ctl00$c_PasswordTextBox']").send_keys('password')
    driver.find_element(By.CSS_SELECTOR,"input[value='Login to CORE']").click()       
             
    def check_CaseStatus(self,case_Id,case_Status,tenant_Lispendens_caseDetails):
        try:
            if (case_Status=='OPEN'):
                print(case_Status)
                tenant_Lispendens_caseDetail = [
                        {'Case_ID': case_Id, 'Case_Status': case_Status,},
                            
                            ]
                tenant_Lispendens_caseDetails+=tenant_Lispendens_caseDetail                
                self.driver.refresh()
            else:
                self.driver.refresh() 
        except NoSuchElementException:
            self.driver.refresh()           
    def tenant_Lispendens_SearchCaseStatus(self,tenant_And_Lispendens_ExtractionFilepath,case_Details,csv_FileName):
        try:
            teant_Lispendens_caseDtaills=[]
            today_dateTime = date.today()
            today_Date = today_dateTime.strftime("%d-%m-%Y")
            tenant_FileName="tenant-"+today_Date+".csv"
            lispendens_FileName="lispendens-"+today_Date+".csv"
            for case_Detail in case_Details:
                case_Number=case_Detail['CaseNumber']
                file_date_time=case_Detail['FileDate'].split(' ')
                file_Date=file_date_time[0]
                self.driver.find_element(By.CSS_SELECTOR,'body > form:nth-child(1) > div:nth-child(35) > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) \
                > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > input:nth-child(1)').send_keys(case_Number)
                self.driver.find_element(By.CSS_SELECTOR,'body > form:nth-child(1) > div:nth-child(35) > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) \
                > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > input:nth-child(1)').click()
                case_Id = self.driver.find_element(By.XPATH,("//span[@id='c_CaseNumberLabel']")).text
                print(case_Id)
                case_Status = self.driver.find_element(By.XPATH,("//div[@class='caseDisplayTable caseSummary']/table/tbody/tr[2]/td[2]")).text
                print(case_Status)
                if(csv_FileName==tenant_FileName):
                    if(file_Date==today_Date):    
                        if (case_Status=='OPEN'):
                                petitioner_Name = self.driver.find_element(By.XPATH,("//div[@class='caseDisplayTable']/table/tbody[2]/tr/td[1]")).text
                                party_type = self.driver.find_element(By.XPATH,("//div[@class='caseDisplayTable']/table/tbody[2]/tr/td[2]")).text
                                petitioner_Address = self.driver.find_element(By.XPATH,("//div[@class='caseDisplayTable']/table/tbody[2]/tr/td[3]")).text
                                tenant_CaseDetail= [
                                                {'Case_ID': case_Id, 'Case_Status': case_Status, 'Petitioner_Name': petitioner_Name, 'Party_Type':party_type, 'Address':petitioner_Address},
                                                ]
                                teant_Lispendens_caseDtaills+=tenant_CaseDetail
                                self.driver.refresh()   
                        else:    
                            self.driver.refresh() 
                        csv_Headings = tenant_CaseDetail[0].keys()
                    elif(case_Status=='OPEN'):
                        obj.check_CaseStatus(case_Id,case_Status,teant_Lispendens_caseDtaills)
                        self.driver.refresh()
                    else:
                        self.driver.refresh()
                    #csv_Headings = teant_Lispendens_caseDtaills[0].keys()              
                elif(csv_FileName==lispendens_FileName):            
                    if (case_Status=='OPEN'):
                        obj.check_CaseStatus(case_Id,case_Status,teant_Lispendens_caseDtaills)
                        self.driver.refresh()
                    else:
                        self.driver.refresh()
                    csv_Headings = teant_Lispendens_caseDtaills[0].keys()      
    
        except NoSuchElementException:
            self.driver.refresh()
        
        with open(f'{tenant_And_Lispendens_ExtractionFilepath}convertfile.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, csv_Headings)
            dict_writer.writeheader()
            dict_writer.writerows(teant_Lispendens_caseDtaills)
        
            
obj=tenant_And_Lispendens()           
app=Flask(__name__)
app.config["UPLOAD_FOLDER"]="Dual_court/Upload Excel File/static"
@app.route("/",methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        upload_file = request.files['upload_excel']
        if upload_file.filename != '':
            tenant_Lispendens_CsvfilePath = os.path.join(app.config["UPLOAD_FOLDER"],'excel', upload_file.filename)
            upload_file.save(tenant_Lispendens_CsvfilePath)
            case_Details=[*csv.DictReader(open(tenant_Lispendens_CsvfilePath))]
            global csv_FileName            
            csv_FileName=os.path.basename(tenant_Lispendens_CsvfilePath)
            tenant_And_Lispendens_ExtractionFilepath=os.path.join(app.config["UPLOAD_FOLDER"],'convertExcel',upload_file.filename)
            obj.tenant_Lispendens_SearchCaseStatus(tenant_And_Lispendens_ExtractionFilepath,case_Details,csv_FileName)     
    return render_template("UploadExcel.html")

@app.route('/download')
def download_file(): 
    print(csv_FileName)
    csv_filname=csv_FileName+"convertfile.csv"
    file=os.path.join('static','convertExcel',csv_filname)
    print(file)
    return send_file(file, as_attachment=True)

    
if __name__=='__main__':
    app.run(debug=True)

       
            
        


    
                
    


















