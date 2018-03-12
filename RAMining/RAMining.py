## THIS CODE REQUIRES PYTHON 2.7

import globalParser
import nolioRequestParser
import perfmon
import globalValidation
class RAMining:
    globalParse=globalParser.CommonParser()
    nolioreq=nolioRequestParser.NolioRequest()
    globalVal=globalValidation.LogValidator()
    perfmonParse=perfmon.PerfMon() 
    noliorequestfpath="C://Cases//BNPP//00978842//custom_nolio_request.log"
    perfmonfpath="C://Cases//BNPP//00978842"
    dPath="C://Cases//BNPP//00978842"
    headers=['Log Name','Date','Time','Thread','Log Level','Protocol','Method','CODE','API','User','RemoteHost','RemoteAddress','X-Forwarded-For','START_DATE','START_TIME','Duration']
    ##This is for nolio performance logs ##
    #perfmonParse.resourceInsight(perfmonfpath,"nolio_perf_mon_nac.log")
    #globalParse.writeCSV(temp,"perfmon.csv",perfmonfpath,seperator=',', headers=[])
    globalParse.releaseCreated("C://Cases//BNPP//00978842//Incident-20180306-0978842//20180306")
    #THIS IS TO CAPTURE THE NOLIO_REQUEST.LOG IN TO PARSABLE FORM
    lines=globalParse.fileReader(noliorequestfpath)
    temp=globalParse.columnParser("custom_nolio_request.log",lines)
    globalParse.writeCSV(temp,"testing.csv",dPath,seperator=',', headers=headers)
    
    #6.2 and Higher##['Log Name','Date','Time','Thread','Log Level','Protocol','Method','CODE','API','User','RemoteHost','RemoteAddress','X-Forwarded-For','START_DATE','START_TIME','Duration']
    #5.5.2 and Higher##['Log Name','Date','Time','Thread','Log Level','Protocol','Method','CODE','API','User','RemoteHost','RemoteAddress','START_DATE','START_TIME','Duration']
    
    temp=globalParse.readCSVAsDict(dPath+"//testing.csv")
    nolioreq.engagementInsight(temp,dPath,"engagementInsight.csv",headers=headers)
    nolioreq.featureInsight(temp,dPath,"featureInsight.csv",headers=['Date','API'])
    #THIS IS TO CHECK HOW MUCH TIME DOES REPORTING API TOOK TIME TO PROCESS
    temp=globalParse.apiParser(dPath,"testing.csv",'a/reports/releasesReportsPage');
    releaseTemp=globalParse.apiParser(dPath,"testing.csv",'a/deployments/[0-9]*$',pattern=True);
    globalParse.writeCSV(temp,"apiInsight.csv",dPath,seperator=',', headers=['Date-Time','User','API','TimeTaken(seconds)'])
    globalParse.writeCSV(releaseTemp,"release_created.csv",dPath,seperator=',', headers=['Date-Time','User','API','TimeTaken(seconds)'])
    

    #globalVal.timeOrderValidator("C://Cases//ING//00686751//logsplainapp//logsplainapp",["C://Cases//ING//00686751//logsplainapp//logsplainapp"])
    #globalVal.timeOrderValidator("C://Saurabh//Movies//EURO Issue",["C://Saurabh//Movies//EURO Issue//logs_primaryNAC//logs","C://Saurabh//Movies//EURO Issue//logs_secondaryNAC//logs"])
    #globalParse.releaseIdParser(dPath,64149431)
    #globalParse.processIdParser('releaseDetails.txt',"C://Cases//Swisscom//00580829//NolioAutomationCenterLogs",'12863')

