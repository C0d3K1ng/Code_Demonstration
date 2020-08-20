#!/usr/bin/env python3
#Import Modules
import csv
import operator
import re 
import sys

#Initialize dictionaries
error = {}
per_user = {}
#Regex formulas 
errorFound = r"ticky: ERROR: ([\w]*) \((.+)\)"
infoFound = r"ticky: INFO: ([\w]*)"

with open("syslog.log", "r") as file:
    #iterate through log files
    for line in file.readlines():
        if re.search(errorFound, line):
            capture = re.search(errorFound, line)
            error.setdefault(capture.group(1),0)
            error[errormsg.group(1)]+=1
            per_user.setdefault(capture.group(2),[0,0])[1]+=1
        if re.search(infoFound, line):
            capture = re.search(infoFound, line)
            per_user.setdefault(capture.group(1),[0,0])[0]+=1
     
    
#Sorting 
sortError=sorted(error.items(), key = operator.itemgetter(1), reverse= True)
sortUser=sorted(per_user.items())
print(sortError)
print(sortUser)
file.close()
 
#CSV Filing 
with open("user_statistics.csv", "w") as userFile:
    writeUsers = csv.writer(userFile)
    writeUsers.writerow(["Username", "INFO", "ERROR"])
    for user in sortUser:
        rows = ([user[0], user[1][0], user[1][1]])
        writeUsers.writerow(rows)
userFile.close()

with open("error_message.csv", "w") as errorFile:
    writeErrors= csv.writer(errorFile)
    writeErrors.writerow(["Error", "Count"])
    writeErrors.writerows(Sorterror)
errorFile.close()    