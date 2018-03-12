import fileinput
import re
import os
import csv
import fnmatch

os.chdir('C://Cases//Tesco//00485742//')
headers=['Log Name','Date','Start Time','Thread','Log Level','Protocol','Method','API','User','Remote','End Time','Duration']
temp_list=[]
headerFlag=False
if os.path.exists('test1.csv'):
    fp= open(b'test1.csv','a')
else:
    fp= open(b'test1.csv', 'w')
    headerFlag=True
a = csv.writer(fp, delimiter=',')
if headerFlag==True:
     temp_list.append(headers)
directoryList=["C://Cases//Tesco//00485742//6Oct//DMS1","C://Cases//Tesco//00485742//6Oct//DMS2"]
for dir in directoryList:
    parse_Files=[]
    os.chdir(dir)
    logSource=dir.rsplit('/').pop()
    fileList=os.listdir(os.path.abspath(dir))
    for f in fileList:
        if fnmatch.fnmatch(f, "nolio_requests.*"):
            parse_Files.append(f)
    
    lines = list(fileinput.input(parse_Files))
    for l in lines:
        ll=re.sub('\[|\]|[A-Za-z]+:\s|USER|Remote|ms|START|(\d\d/){2}\d\d\d\d','',l).split()
        ll.remove('-')
        ll.insert(0,logSource)
        temp_list.append(ll)
    a.writerows(temp_list)

fp.close()