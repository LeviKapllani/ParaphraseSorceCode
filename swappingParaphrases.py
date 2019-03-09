from editPairs import *
import numpy as np

def newPhrases(s1,s2):
    s = init_scanner()
    p1 = s.scan(s1)[0]
    p2 = s.scan(s2)

    s = init_scanner()
    p1 = s.scan(s1)[0]
    p2 = s.scan(s2)[0]
    # Get a tokenized (key,value) tuple for each token in a paraphrase line

    vars1 = getVars(p1)
    vars2 = getVars(p2)
    # Get the variables from each paraphrase line

    p1Value = [x[1] for x in p1]
    p2Value = [x[1] for x in p2]
    # Get the values for each paraphrase line

    if len(vars1) == len(vars2) and len(np.unique(vars1)) == len(np.unique(vars1)) and len(vars1) != 0:
        varPairs = list(zip(vars1, vars2))
        varPairs = list(set(varPairs))
        # newPOneValues = p1Value
        # newPTwoValues = p2Value

        newPOneValues = swap(p2Value, varPairs)
        newPTwoValues = swap(p1Value, varPairs)

        return newPOneValues, newPTwoValues
    else:
        return [],[]


def swap(pValue,varPairs):
#Given a phrase and pairs of variables swap their variables to create two new phrases.
    newPhrase = [''] * len(pValue)
    modifiedFlag = np.zeros(len(pValue))

    for (var1,var2) in varPairs:
        for i,token in enumerate(pValue):
            if modifiedFlag[i] != 1:
                if token == var1:
                    newPhrase[i] = var2
                    modifiedFlag[i] = 1
                elif token == var2:
                    newPhrase[i] = var1
                    modifiedFlag[i] = 1
                else:
                    newPhrase[i] = token
    if newPhrase == []:
        return pValue
    return newPhrase

# def swap(pValue,varPairs):
# #Given a phrase and pairs of variables swap their variables to create two new phrases.
#     newPhrase = pValue
#     for (var1,var2) in varPairs:
#         newPhrase[newPhrase == var1] = var2
#     return newPhrase
#Experimenting with this; not sure if it works but it should do the same thing as the swap above
