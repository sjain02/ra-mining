import os
from raMiningUtilites import RAUtilities
import csv
import collections
import fnmatch
class PerfMon:
    def resourceInsight(self, directory,filename, overwrite=False,sort=True,headers=[]):
        os.chdir(directory)
        temp_list=[]
        result=True
        if os.path.exists('perfmon.csv'):
            fp= open(b'perfmon.csv','a')
        else:
            fp= open(b'perfmon.csv', 'w')
        parse_Files=[]
        fileList=os.listdir(os.path.abspath(directory))
        for f in fileList:
            if fnmatch.fnmatch(f, "nolio_perf_mon_nac.*"):
                parse_Files.append(f)
        #1: Sort the file from largest to smallest
        raUtilityObj=RAUtilities();
        tempParseFiles=parse_Files;
        tempParseFiles.remove("nolio_perf_mon_nac.log");
        tempParseFiles.sort(key=raUtilityObj.sortFileIndex,reverse=True)
        parse_Files=tempParseFiles
        parse_Files.insert(len(parse_Files),"nolio_perf_mon_nac.log")
        insightDict={}
        for row in listDict:
                getTime=row['Time'].rpartition(',')[0]
                key=row['Date'] + " " + getTime
                if not insightDict.has_key(key):
                    insightDict.update({key:1})
                else:
                    value=insightDict.get(key)
                    value+=1
                    insightDict.update({key:value})
        gb=globalParser.CommonParser()
        gb.writeDictCSV(directory,filename,overwrite,sort,**insightDict)