import os
import shutil

source='c:/users/ayanU/Desktop'
destination='c:/users/ayanU/Desktop/text'

#change the directory
os.chdir(source)

#look for text files
files=os.listdir(source)

#list of file formats
text_formats=["txt","py"]

#make a loop to check all files and if txt or py file move to destination
for file in files:
    file_ext=file.split('.')[-1]
    if file_ext in text_formats:
        shutil.move(file,destination)
        