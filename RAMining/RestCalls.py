import requests
import time
url="http://10.151.16.149:8080/datamanagement/design/parameterFolders"
arrayList=['K','L','M','R','S','T','U','V','W','X','Y','Z']
headcount=0
while headcount < len(arrayList):
    time.sleep(10)
    parentFolderId=""
    data='{"parentFolderId":"13241","@type":"CREATE_FOLDER","parameterFolder":{"name":"'+arrayList[headcount]+'","description":"create via code","containerId":"57","containerType":1}}'
    with requests.Session() as  session:
            session.auth=('superuser','suser')
            session.headers.update({'content-type':'application/json'})   
            response=session.post(url,data)
            if response._content:
                parentFolderId=(response._content.split('"id":'))[1].split(',')[0].replace('"','')
                print("Created parent with id :",parentFolderId," ", response._content)
    count=1
    while count < 500:
        time.sleep(15)
        data='{"parentFolderId":"'+parentFolderId+'","@type":"CREATE_FOLDER","parameterFolder":{"name":"'+arrayList[headcount]+'.'+str(count)+'","description":"","containerId":"57","containerType":1}}'
        with requests.Session() as  session:
            session.auth=('superuser','suser')
            session.headers.update({'content-type':'application/json'})   
            response=session.post(url,data)
            print("Created :",count," request")
        count+=1
    headcount+=1;