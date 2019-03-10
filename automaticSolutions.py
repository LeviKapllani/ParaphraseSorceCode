from newSolutions import *
import itertools
import glob

path = '/Users/lk489/Desktop/ParaphraseSorceCode/test/smallcpp/*'
dirpath = '/Users/lk489/Desktop/ParaphraseSorceCode/test/'
files = glob.glob(path)

firstFile = []
for name in files:
    firstFile.append(name)
secondFile = firstFile

combinedFiles = list(itertools.product(firstFile, secondFile))

for i in combinedFiles:
    if i[0] == i[1]:
        combinedFiles.remove(i)

for i,pair in enumerate(combinedFiles):
    newSolutions(pair[0],pair[1],dirpath +'combination'+str(i+1)+'/',i+1)
    print(i)