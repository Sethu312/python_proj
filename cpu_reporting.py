# Importing the library
import psutil
import datetime
import time
import sys

DPProcesses = [ "omniinet.exe" , "java.exe"  , "postgres.exe",  "crs.exe" , "dbsm.exe"]

cpu_usage_report="c:\\Test\\CPU.csv"

def findProcessIdByName(processName):
    listOfProcessObjects = []
    #Iterate over the all the running process
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name'])
           # Check if process name contains the given name string.
           if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
    return listOfProcessObjects;


for x in DPProcesses: 
    listOfProcessIds = findProcessIdByName(x)
    if len(listOfProcessIds) > 0:
        for elem in listOfProcessIds:
            processID = elem['pid']
            processName = elem['name']
            p = psutil.Process(processID)
            current_time = datetime.datetime.now()
            formattedTime = current_time.strftime("\"%d-%m-%y %H:%M\"")
            print(formattedTime, processName, p.cpu_percent(interval=1))
            # with open(cpu_usage_report, "a") as external_file:
                # print(formattedTime, processName, p.cpu_percent(interval=1)  / psutil.cpu_count(), file=cpu_usage_report)
            f = open(cpu_usage_report, 'a')
            print("\n")
            print(formattedTime+",", processName+",", p.cpu_percent(interval=1)  / psutil.cpu_count(), file = f)
    else :
        print('No Running Process found with given text')
