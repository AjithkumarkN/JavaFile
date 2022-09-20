import enum
import pytesseract
from pdf2image import convert_from_path
import glob
all_files = glob.glob("D:\AK\Pdf_to_text\pdfs\*")

for file in all_files:
    
  
    if '.pdf' in str(file):
        pages = convert_from_path(file, 500)

        for pageNum,imgBlob in enumerate(pages):
            text = pytesseract.image_to_string(imgBlob, lang='eng')
            with open(f'{file}.txt', 'a') as the_file:
                the_file.write(text)
                print(text)

f=open(f'{file}.txt','r')
word=input("enter the keyword:")

count=1
Line=f.readlines()

for line in Line:
    lines=line.split()
    if word in lines:
       
        print('line  number:',count,':',line)
      
    count+=1
    

               
'''if '.png' in str(file):
        image_text = pytesseract.image_to_string(file)
        with open(f'{file}.txt','w') as the_file:
            the_file.write(image_text)''' 