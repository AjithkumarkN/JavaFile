from ExtractZipFile import *
import xmltodict
#import os
import csv
class ConvertXmlToCsv():
    xml_path=ExtractZipFile.xml_path
    download_path=ExtractZipFile.download_path
    filename=ExtractZipFile.filename    
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
    csvfile_path=os.path.join(download_path,filename+'.csv')
    with open(csvfile_path, 'w',newline="") as csvfile_write:
        caseDetail_write = csv.writer(csvfile_write)
        caseDetail_write.writerow(HEADERS)
        caseDetail_write.writerows(filerows)
    os.remove(xml_path)