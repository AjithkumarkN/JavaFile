from flask import Flask,render_template,request
import os
import pandas as pd
import csv


app=Flask(__name__)#get file name and stored app


app.config["UPLOAD_FOLDER"]="Dual_court/Upload Excel File/static/excel"
@app.route("/",methods=['GET','POST'])#router define / mean home page
def upload():
    if request.method == 'POST':
        upload_file = request.files['upload_excel']
        if upload_file.filename != '':
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], upload_file.filename)
            upload_file.save(file_path)
            case_Details=[*csv.DictReader(open(file_path))]            
            for case_Detail in case_Details:
                case_Number=case_Detail['CaseNumber']
                file_date_time=case_Detail['FileDate'].split(' ')
                file_Date=file_date_time[0]
                print(case_Number)
                print(file_Date)
            
            #data=pd.read_excel(upload_file)
            #return render_template("ExcelFile.html",data=data.to_html(index=False).replace('<th>','<th style="text-align:center">'))
    return render_template("UploadExcel.html")


if __name__=='__main__':#app run while appname is main
    app.run(debug=True)
    