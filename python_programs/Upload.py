from flask import Flask,render_template,request,send_file,send_from_directory,session
import os
import pandas as pd
app=Flask(__name__)#get file name and stored app
app.config["UPLOAD_FOLDER"]="Dual_court/Upload Excel File/static"
@app.route("/",methods=['GET','POST'])#router define / mean home page
def upload():
    if request.method == 'POST':
        upload_file = request.files['upload_excel']
        if upload_file.filename != '':
            file_path = os.path.join(app.config["UPLOAD_FOLDER"],'convertExcel', upload_file.filename)
            upload_file.save(file_path)
            global csv_filename
            csv_filename=os.path.basename(file_path)
            print(csv_filename)    
    return render_template("UploadExcel.html")
@app.route('/download')
def download_file(): 
    print(csv_filename)
    csv_file=csv_filename+"convertfile.csv"
    file=os.path.join('static','convertExcel',csv_file)
    print(file)
    return send_file(file, as_attachment=True)


if __name__=='__main__':#app run while appname is main
    app.run(debug=True)
