import os
from datetime import datetime

files = os.listdir('input/')
string = ''
for file in files:
    file = open('input/'+file)
    for line in file:
        string += line

logFile = open('logs/sys.log', 'a+')
word = 'Python'
count = 0
lines = []
found = False
for item in string.splitlines():
    if item.find(word) != -1:
        lines.append(item)
        count += 1
        found = True
if found:
    logFile.write('['+str(datetime.now())+'] Info: Count of (' + word + "), " + str(count) + '\n')
    for line in lines:
        logFile.write('['+str(datetime.now())+'] Info: line, ' + line + '\n')
else:
    logFile.write('['+str(datetime.now())+'] Error: There are no result!' + '\n')
