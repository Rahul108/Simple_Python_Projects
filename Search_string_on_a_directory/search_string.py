import sys
import glob, os
from fnmatch import fnmatch

def searchStringFromFile(fileName,stringToSearch):
    with open(fileName,'r') as txtFile:
        lineList = []
        i = 0
        for line in txtFile:
            lineList.append(line.rstrip("\n"))
            if stringToSearch in lineList[i]:
                print("On Line: ",i)
                print(lineList[i],"\n")
            i+=1


def selectDirectory(directoryToExplore, searchString, formatOfFiles):
    for path, subdirs, files in os.walk(directoryToExplore):
        for name in files:
            if fnmatch(name, formatOfFiles):
                print("=======================")
                print(path)
                # print(files)
                for i in range(len(files)):
                    try:
                        fileNameWithDirectory = path + "/" + files[i]
                        searchStringFromFile(fileNameWithDirectory,searchString)
                    except:
                        print(files[i]," not accessable -_- ")
                    
                print("=======================\n\n")
                

def run():
    directory = sys.argv[1]
    searchString = input("Enter a String to Search: ")
    formats = ['*.txt','*.py','*.smali','*.xml']
    for ff in range(len(formats)):
        selectDirectory(directory, searchString, formats[ff])


run()

