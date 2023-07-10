"""
Author: Ian Bartlow
Last Edited: 7/10/23
Descrption: A simple script that pulls the number of course openings based on course type
done via webscraping with regex
"""

import re
import urllib.request
import xlwt
from xlwt import Workbook


# used to write to a spreadsheet
workBook = Workbook()
sheet = workBook.add_sheet("Course Modes")

"""
Keys are based on course type
Keys:
F2F = Face To Face
HYB = Hybrid
OL = Online
SOL = Synchronous Online
FLX = Flex Course
"""
modeDict = {"F2F": 0, "HYB": 0, "OL": 0, "SOL": 0, "FLX": 0}


# url where we are pulling the html from
dataUrl = "https://rosters.wilkes.edu/scheds/coursesF22.html"
data = urllib.request.urlopen(dataUrl).read().decode("utf-8")
data = data.split()


# checks each line using a regex
# if the line has a mode in it, save it in a string
# if the line has a number in it, add it to that dictionary value accessed via
# the string
# if the line has nothing we want, do nothing
for i in data:
    match = re.search(">(...)</span>|>(OL)</span>", i)
    match2 = re.search('"text-end">\d</td>|"text-end">\d\d', i)

    if match:
        if i[7:10] == "FLX":
            key = "FLX"
        elif i[7:10] == "F2F":
            key = "F2F"
        elif i[7:10] == "SOL":
            key = "SOL"
        elif i[7:10] == "HYB":
            key = "HYB"
        elif i[7:9] == "OL":
            key = "OL"

    if match2:
        if len(i) == 26:
            modeDict[key] = modeDict[key] + int(i[17])
        elif len(i) == 27:
            modeDict[key] = modeDict[key] + int(i[17:19])
        elif len(i) == 28:
            if i[17:20] == "0</":
                pass
            else:
                modeDict[key] = modeDict[key] + int(i[17:20])


print(modeDict)

counter = 0
for key in modeDict:
    sheet.write(0, counter, key)
    sheet.write(1, counter, modeDict[key])
    counter += 1


# writes to courseSheet.xls in active directory
workBook.save("courseSheet.xls")
