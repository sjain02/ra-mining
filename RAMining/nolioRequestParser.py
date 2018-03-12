import globalParser
class NolioRequest:
    def engagementInsight(self, listDict,directory,filename, overwrite=False,sort=True,headers=[]):
        insightDict={}
        for row in listDict:
                #engagement insight per Seconds
                getTime=row['Time'].rpartition(',')[0]
                #engagement insight per Minute
                getTime=getTime.rpartition(':')[0]
                key=row['Date'] + " " + getTime
                if not insightDict.has_key(key):
                    insightDict.update({key:1})
                else:
                    value=insightDict.get(key)
                    value+=1
                    insightDict.update({key:value})
        gb=globalParser.CommonParser()
        gb.writeDictCSV(directory,filename,overwrite,sort,**insightDict)
    def featureInsight(self, listDict,directory,filename, overwrite=False,sort=True,headers=[]):
        engagementDict={}
        for row in listDict:
                partitions=row['API'].rpartition('datamanagement')
                key=partitions[len(partitions)-1]
                if not engagementDict.has_key(key):
                    engagementDict.update({key:1})
                else:
                    value=engagementDict.get(key)
                    value+=1
                    engagementDict.update({key:value})
        gb=globalParser.CommonParser()
        gb.writeDictCSV(directory,filename,overwrite,sort,**engagementDict)
    def usersInsight(self, listDict,directory,filename, overwrite=False,sort=True,headers=[]):
        pass
    def protocolInsight(self, listDict,directory,filename, overwrite=False,sort=True,headers=[]):
        pass
    
