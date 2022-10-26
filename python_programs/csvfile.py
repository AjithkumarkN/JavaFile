import os
import csv
pathname=os.path.dirname(os.path.abspath(__file__))
completepath=os.path.join(pathname,'paofiles',"PAO - Sheet1.csv")#read csv file path location
lst=[*csv.DictReader(open(completepath))]
for i in lst:
    address=i['Primary Residence'].split(" ")#coloum name split by space
    address_no=address[0]
    address_street=address[2]
    zipcode=i['PrimaryResidenceZip']
    print(address)
    print(zipcode)
    print(address_no)
    print(address_street)