import sys
import fileinput
import re
import csv
import collections
import fnmatch
import os
from raMiningUtilites import RAUtilities
class CommonParser:
    def columnParser(self,logsource,lines,pattern='\[|\]|[A-Za-z]+:\s|USER|REMOTE|ms|START|STATUS|X-Forwarded-For(.)', replacement=''):
        #pattern eating releasenumbers \[|\]|[A-Za-z]+:\s|USER|REMOTE|ms|START|STATUS|X-Forwarded-For(.)|(\d\d){2}\d\d\d\d
        #USER|REMOTE|ms|START|X-Forwarded-For|(\d\d){2}\d\d\d\d
        #NEW:- \[|\]|[A-Za-z]+:\s|USER|REMOTE|ms|START|STATUS|X-Forwarded-For(.)|(\d\d){2}\d\d\d\d
        #OLD: -\[|\]|[A-Za-z]+:\s|USER|REMOTE|ms|START|(\d\d/){2}\d\d\d\d
        temp_list=[]
        for l in lines:
            ll=re.sub(pattern,replacement,l).split()
            ll.remove('-')
            ll.insert(0,logsource)
            temp_list.append(ll)  
        return temp_list
    def fileReader(self,filePath):
        lines = list(fileinput.input(filePath))  
        return lines
    def writeCSV(self,lines,filename,directory, overwrite=False, seperator=";", headers=[]):
        """ 
            If file exist, write will append to existing file else will create new. 
            In case of overwrite mentiond overwrite=True.
        """
        fp=RAUtilities().FileHandle(directory,filename,overwrite)
        if (len(headers)>0):
                lines.insert(0,headers)
        a = csv.writer(fp, delimiter=seperator)        
        a.writerows(lines)
        fp.close()
    def readCSVAsDict(self,filePath):
        with open(filePath) as csvfile:
            reader=csv.DictReader(csvfile)
            dictList=list(reader)
        return dictList
    def writeDictCSV(self,directory,filename,overwrite=False,sort=True,**dict):
        if sort==True:
            od=collections.OrderedDict(sorted(dict.items()))
        else:
            od=collections.OrderedDict(dict.items())
        fp=RAUtilities().FileHandle(directory,filename,overwrite)
        writer = csv.writer(fp)
        for key,value in od.items():
            writer.writerow([key,value])
        fp.close()
    def releaseIdParser(self,directory,releaseId):
        if releaseId !=0:
            searchString=["\"releaseId\":\""+str(releaseId)+"\"",str(releaseId)]
            parse_Files=[]
            temp_list=[]
            os.chdir(directory)
            fileList=os.listdir(os.path.abspath(directory))
            for f in fileList:
                if fnmatch.fnmatch(f, "nolio_dm_all.*"):
                    parse_Files.append(f)
            parse_Files.sort()
            parse_Files.reverse()
            lines = list(fileinput.input(parse_Files))
            for l in lines:
                #ll=re.search(searchString,l)
                if re.search(searchString[0],l) or re.search(searchString[1],l):
                    temp_list.append(l)
            fp= open(b'releaseDetails.txt', 'w')
            fp.writelines(temp_list)
            fp.close()
            self.processIdParser('releaseDetails.txt',directory,releaseId)

    def releaseCreated(self,directory):
        searchString=["created\s\[ReleaseImpl\{id=[0-9]*"] 
        parse_Files=[]
        temp_list=[]
        os.chdir(directory)
        fileList=os.listdir(os.path.abspath(directory))
        for f in fileList:
            if fnmatch.fnmatch(f, "nolio_dm_all.*"):
                parse_Files.append(f)
        parse_Files.sort()
        parse_Files.reverse()
        lines = list(fileinput.input(parse_Files))
        for l in lines:
            #ll=re.search(searchString,l)
            if re.search(searchString[0],l) :
                temp_list.append(l)
        fp= open(b'release_created_Details.txt', 'w')
        fp.writelines(temp_list)
        fp.close()
            
    def apiParser(self,directory,fileName,api,pattern=False):
        if api !="":
            searchString=api
            dictLines=self.readCSVAsDict(directory+"//"+fileName)
            os.chdir(directory)
            temp_list=[]
            for row in dictLines:
                ll=[]
                apiUrl=row['API']
                checkCondition=False
                if(pattern==False):
                    checkCondition=apiUrl.find(api)!=-1
                else:
                    checkCondition=re.search(api,apiUrl)!=None
                if(checkCondition):
                    ll.append(row['Date']+" "+ row['Time'])
                    ll.append(row['User'])
                    ll.append(row['API'])
                    #dont conver the time in minutes
                    #ll.append((int(row['Duration'])/1000))
                    ll.append(row['Duration'])
                    temp_list.append(ll)
            return temp_list

    def processIdParser(self, fileName,directory,releaseId):
        processIds={}
        temp_list=[]
        os.chdir(directory)
        lines = list(fileinput.input(fileName))
        for l in lines:
            splitted=l.split('body=')
            body=(splitted[len(splitted)-1]).split('}\'')[0]
            body=body.replace('"','')
            body=body.replace('\'{','')
            temp_list.append(body+"\n")
        f=str(releaseId)+'jobDetails.txt'
        fp= open(f, 'w')
        fil=list(set(temp_list))
        fp.writelines(fil)
        fp.close()
            
        