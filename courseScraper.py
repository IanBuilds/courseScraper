import re
import urllib.request
modeDict={
    "F2F":0,
    "HYB":0,
    "OL":0,
    "SOL":0,
    "FLX":0
}

dataUrl = "https://rosters.wilkes.edu/scheds/coursesF22.html"
data = urllib.request.urlopen(dataUrl).read().decode('utf-8')

data = data.split()


#idea: check each line using a regex
#if the line has a mode in it, save it in a string
#if the line has a number in it, add it to that dictionary value accessed via
#the string
#if the line has nothing we want, do nothing
for i in data:
    match = re.search('>(...)</span>|>(OL)</span>', i)
    match2 = re.search('"text-end">\d</td>|"text-end">\d\d',i)

    if(match):
        if(i[7:10]=='FLX'):
            key = 'FLX'
        elif(i[7:10]=='F2F'):
            key = 'F2F'
        elif(i[7:10]=='SOL'):
            key = 'SOL'
        elif(i[7:10]=='HYB'):
            key = 'HYB'
        elif(i[7:9]=='OL'):
            key = 'OL'

    if(match2):

        if((len(i) == 26)):
            modeDict[key] = modeDict[key] + int(i[17])
        elif((len(i) == 27)):
            modeDict[key] = modeDict[key] + int(i[17:19])
        elif((len(i) == 28)):
            if(i[17:20] =='0</'):
                pass
            else:
                modeDict[key] = modeDict[key] + int(i[17:20])

print(modeDict)
