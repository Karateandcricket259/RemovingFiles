import os
import shutil
import time
path1="/Users/rajiv/Eashan/Python/txt/sample2.txt"
path=input("Enter the name of the directory")
days=input("Enter how many days old is the file")
days = int(input("Input days: ")) * 3600 * 24
storing=os.listdir(path)
for file in storing:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext=='':
        continue
if os.path.exists(path+'/'+ ext):
     shutil.move(path+'/'+ file, path+'/'+ext+'/'+ file)
os.path.join(path1,removefiles.py)
ctime= os.stat(path).st_ctime
return ctime

if os.path.notexists():
    print("Path not found")