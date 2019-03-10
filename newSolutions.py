from swappingParaphrases import *
import os
import errno
import shutil


def newSolutions(file1,file2,dirName,combinationNumber):

    filePhraseDict = {}
    fileNumber = 1

    f1sentences = getFileLines(file1)
    f2sentences = getFileLines(file2)

    pairs = SharedSmallestLevenshteinPairs(f1sentences, f2sentences)

    try:
        os.mkdir(dirName)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass

    for pair in pairs:
        filePhraseDict[pair[0]] = file1
        filePhraseDict[pair[1]] = file2

        newPOneValues, newPTwoValues =  newPhrases(pair[0],pair[1])
        phrases = [newPOneValues, newPTwoValues]

        if newPOneValues != []:
            for i,phrase in enumerate(phrases):
                newPhase = ''.join(map(str, phrase)).replace(" ", "")
                currentPhase = pair[i].replace(" ", "")
                if newPhase != currentPhase :
                    currentFile = filePhraseDict[pair[i]];
                    shutil.copy(currentFile, dirName)
                    with open(currentFile) as f:
                        filename = 'solution' + str(combinationNumber) + '-' + str(fileNumber)+".cpp"
                        filepath = os.path.join(dirName, filename)
                        with open(filepath, "w") as f1:
                            for line in f:
                                if line.lstrip().strip('\n') == pair[i]:
                                    f1.write(' '.join(map(str, phrase)) + '\n')
                                else:
                                    f1.write(line)
                        fileNumber += 1
                        f1.close()
                        f.close()
