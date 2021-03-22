import os
import csv
import shutil


files = os.scandir() #iterates/scans through every file and folder in pop export 
dirList = []

for g in files:
    if g.is_dir(): #check if it is folder
        dirList.append(g)


for k in dirList:
    folderfiles = os.scandir(path=k.name) #specify you're scanning within folder k only
    for f in folderfiles:
        print(f) #gives visual indication our program is running and not stuck on a loop
        if '.csv' not in f.name: #just in case a random file that isn't a .csv is in the folder(it shouldn't be)
            continue
        firstRowCheck = True #first line is the header, lets us ignore header
        with open(f.name, newline='') as sourceFile:
            with open(f.name+'output.csv', mode = 'w', newline='') as outputFile: #syntax for opening a .csv file to read from and write from
                reader = csv.reader(sourceFile, delimiter =' ', quotechar ='|')
                writer = csv.writer(outputFile) #more syntax, lifted directly from documentation
                first = 1 #first scraped entry per day
                last = 1 #last scraped entry per day
                currentDate = 0
                for row in reader:
                    if firstRowCheck: #checks if this is the first row and skips it
                        firstRowCheck = False
                        continue
                    if row[0] != currentDate:
                        sanitizedDate = str(currentDate).strip('"') #makes it a little better to look at, removes quotes from beginning
                        if first == '0' or last == '0': #sometimes we start off with 0 users holding, so this takes of it
                            first = 1 #needs improvement to indicate
                            last = 1
                        perchange = ((int(last)-int(first))/int(first)) * 100
                        writer.writerow([sanitizedDate, perchange])
                        currentDate = row[0]
                        firstindex = row[1].index(',') #more cleanliness of data
                        first = row[1][firstindex+1:]
                    lastindex = row[1].index(',')
                    last = row[1][lastindex+1:]
        shutil.move(os.path.join(os.getcwd(),f.name+'output.csv'), k) 
