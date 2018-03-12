import sys
import fileinput
import re
import csv
import collections
import fnmatch
import os
from raMiningUtilites import RAUtilities
class LogValidator:
    def timeOrderValidator(self, parentDirectory, directoryList=[]):
        os.chdir(parentDirectory)
        temp_list=[]
        result=True
        if os.path.exists('didDateTimeJumped.txt'):
            fp= open(b'didDateTimeJumped.txt','a')
        else:
            fp= open(b'didDateTimeJumped.txt', 'w')
        for dir in directoryList:
            parse_Files=[]
            os.chdir(dir)
            fileList=os.listdir(os.path.abspath(dir))
            for f in fileList:
                if fnmatch.fnmatch(f, "nolio_dm_all.*"):
                    parse_Files.append(f)
            #1: Sort the file from largest to smallest
            raUtilityObj=RAUtilities();
            tempParseFiles=parse_Files;
            tempParseFiles.remove("nolio_dm_all.log");
            tempParseFiles.sort(raUtilityObj.sortFileIndex,reverse=True)
            parse_Files=tempParseFiles
            parse_Files.insert(len(parse_Files),"nolio_dm_all.log")
            #2: Get the key 
            #3: Compare and write a change....
            dateDict={}
            
            lines = list(fileinput.input(parse_Files))
            for l in lines:
                ll=re.sub('\[|\]|[A-Za-z]+:\s|USER|Remote|ms|START|(\d\d/){2}\d\d\d\d','',l).split()
                if len(ll)>2:
                    if re.match('[0-9].{4}',ll[0]):
                        currentVal=ll[1];
                        currentVal=currentVal.rsplit(',')[0]
                        currentValSplit=currentVal.split(':')    
                        keyValueInsert=currentVal                            
                        if not dateDict.has_key(ll[0]):
                            dateDict.update({ll[0]:currentVal})
                        elif dateDict.has_key(ll[0]):
                            
                            oldValue=dateDict.get(ll[0])
                            oldValueSplit=oldValue.split(':')
                            if (True if (currentValSplit[0]>oldValueSplit[0] or currentValSplit[1]>oldValueSplit[1] or currentValSplit[2]>oldValueSplit[2]) else False):
                                oldLine=l
                                dateDict.update({ll[0]:currentVal})
                            elif (True if (currentValSplit[0]==oldValueSplit[0] or currentValSplit[1]==oldValueSplit[1] or currentValSplit[2]==oldValueSplit[2]) else False):
                                oldLine=l
                            elif (True if (currentValSplit[0]<oldValueSplit[0] or currentValSplit[1]<oldValueSplit[1] or currentValSplit[2]<oldValueSplit[2]) else False):
                                temp_list.append(l)
                                result=False
                                break
        for t in temp_list:           
            fp.write(t)
        fp.close()
        return result