from swappingParaphrases import *


file1 = "BS1.cpp"
file2 = "BS2.cpp"


pairs = []
filePhraseDict = {}
fileNumber = 3;

f1sentences = getFileLines(file1)
f2sentences = getFileLines(file2)

pairs = SharedSmallestLevenshteinPairs(f1sentences, f2sentences)


for pair in pairs:
    filePhraseDict[pair[0]] = file1
    filePhraseDict[pair[1]] = file2

    newPOneValues, newPTwoValues =  newPhrases(pair[0],pair[1])
    phrases = [newPOneValues, newPTwoValues]

    if newPOneValues != []:
        for i,phrase in enumerate(phrases):
            if ''.join(map(str, phrase)) != pair[i]:
                currentFile = filePhraseDict[pair[i]];

                with open(currentFile) as f:
                    with open("BS" + str(fileNumber) +".cpp", "w") as f1:
                        for line in f:
                            if line.lstrip().strip('\n') == pair[i]:
                                f1.write(''.join(map(str, phrase)) + '\n')
                            else:
                                f1.write(line)
                    fileNumber += 1
                    f1.close()
                    f.close()
