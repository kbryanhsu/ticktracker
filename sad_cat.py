import os
import csv

with open('AAL.csv', newline='') as sourceFile:
    with open('AALoutput.csv', mode = 'w', newline='') as outputFile:
        reader = csv.reader(sourceFile, delimiter =' ', quotechar ='|')
        writer = csv.writer(outputFile, quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        first = 1   
        last = 0
        currentDate = 0
        firstRowCheck = True
        for row in reader:
            if firstRowCheck:
                firstRowCheck = False
                continue
            if row[0] != currentDate:
                writer.writerow([currentDate, ((int(last)-int(first))/int(first)) * 100])
                currentDate = row[0]
                firstindex = row[1].index(',')
                first = row[1][firstindex+1:]
            lastindex = row[1].index(',')
            last = row[1][lastindex+1:]

