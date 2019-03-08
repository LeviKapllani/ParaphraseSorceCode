from editPairs import *
import numpy as np

def swap(p1Value,p2Value,varPairs):
#Given two phrases and pairs of variables swap their variables to create two new phrases.
    phraseOne = [];
    phraseTwo = [];
    for (var1,var2) in varPairs:
        if var1 != var2:
            for i,token1 in enumerate(p1Value):
                if token1 == var1:
                    phraseTwo.append(var2)
                else:
                    phraseTwo.append(p1Value[i])
            for j,token2 in enumerate(p2Value):
                if token2 == var2:
                    phraseOne.append(var1)
                else:
                    phraseOne.append(p2Value[j])
    return phraseOne,phraseTwo



s1 = "if (a[j]>a[j+1]){"
s2 = "if (arr[j] > arr[j+1])"

s = init_scanner()
p1 = s.scan(s1)[0]
p2 = s.scan(s2)

s = init_scanner()
p1 = s.scan(s1)[0]
p2 = s.scan(s2)[0]
#Get a tokenized (key,value) tuple for each token in a paraphrase line


vars1 = getVars(p1)
vars2 = getVars(p2)
#Get the variables from each paraphrase line


p1Value = [x[1] for x in p1]
p2Value = [x[1] for x in p2]
#Get the values for each paraphrase line



if len(vars1) == len(vars2) and len(np.unique(vars1)) == len(np.unique(vars1)):
    varPairs = list(zip(vars1, vars2))
    varPairs = list(set(varPairs))
    newPOneValues = p1Value
    newPTwoValues = p2Value


    newPOneValues, newPTwoValues = swap(newPOneValues,newPTwoValues,varPairs)

    if newPOneValues != p1Value and newPTwoValues != p2Value:
        with open("BS1.cpp") as f:
            with open("BS3.cpp", "w") as f1:
                for line in f:
                    currentP = s.scan(line)
                    if currentP == p1:
                        f1.write(newPTwoValues)
                    else:
                        f1.write(line)


