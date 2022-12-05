from FtpFileDownload import *
import zipfile
import os
class ExtractZipFile():
    time.sleep(2)
    download_path=FtpFileDownlod.download_path
    filename=FtpFileDownlod.filename
    zip_path=os.path.join(download_path,filename+'.zip')
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(download_path)
    xsd_path=os.path.join(download_path,filename+'.xsd')
    xml_path=os.path.join(download_path,filename+'.xml')
    os.remove(xsd_path) 
    os.remove(zip_path) 