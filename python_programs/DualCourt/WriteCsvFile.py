from DoualCourtSearch import *
class WriteCsvFile():
    convert_tenantfile=TenantAndLispendens.convert_tenantfile
    convert_lispendensefile=TenantAndLispendens.convert_lispendensefile
    tenant_casedetails=TenantAndLispendens.tenant_casedetails
    lispendense_casedetails=TenantAndLispendens.lispendense_casedetails
    #convert_tenantfile=os.path.join(download_path,'tenent-'+today_Date+'.csv')
    #convert_lispendensefile=os.path.join(download_path,'lispendence-'+today_Date+'.csv')
    csv_Headings=['Case_ID','Case_Status','Petitioner_Name','Party_Type','Address']
    with open(convert_tenantfile, 'w', newline='') as tenant_outputfile:
        tenant_dict_writer = csv.DictWriter(tenant_outputfile, fieldnames=csv_Headings)
        tenant_dict_writer.writeheader()
        tenant_dict_writer.writerows(tenant_casedetails)
    with open(convert_lispendensefile, 'w', newline='') as lispendense_outputfile:
        lispendense_dict_writer = csv.DictWriter(lispendense_outputfile, fieldnames=csv_Headings)
        lispendense_dict_writer.writeheader()
        lispendense_dict_writer.writerows(lispendense_casedetails)