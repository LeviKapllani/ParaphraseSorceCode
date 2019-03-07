import sys
import re
import numpy
import itertools

def init_scanner():
    kwlist = ["asm","else","new","this","auto","enum","operator","throw","bool","explicit","private","true","break","export","protected","try","case","extern","public","typedef","catch","false","register","typeid","char","float","reinterpret_cast","typename","class","for","return","union","const","friend","short","unsigned","const_cast","goto","signed","using","continue","if","sizeof","virtual","default","inline","static","void","delete","int","static_cast","volatile","do","long","struct","wchar_t","double","mutable","switch","while","dynamic_cast","namespace","template","And","bitor","not_eq","xor","and_eq","compl","or","xor_eq","bitand","not","or_eq"]
    s = re.Scanner([
    (r"\"[^\"]*?\"", lambda scanner, token:("String",token)),
    (r"'[^']*?'", lambda scanner, token:("String",token)),
    (r"#.*\n", lambda scanner, token:("Preprocessor Statement",token.strip())),
    (r"//.*(\n|\Z)", lambda scanner, token:("Comment",token.strip())),
    (r"/\*.*\*/", lambda scanner, token:("Comment",token.strip())),
    (r".*\?.*\:.*", lambda scanner, token:("Ternary",token.strip())),
    (r"\s*({})\s".format('|'.join(kwlist)), lambda scanner, token:("Keyword",token.strip())),
    (r"[a-zA-Z_\.]+[0-9]*", lambda scanner, token:("String Literal",token)),
    (r"[0-9]+\.[0-9]+", lambda scanner, token:("Float Literal", token)),
    (r"[0-9]+", lambda scanner, token:("Integer literal", token)),
    (r"\@.*(\s|\n)", lambda scanner, token:("Annotation", token)),
    (r"\(",lambda scanner, token:("Open Parentheses",token)),
    (r"\)",lambda scanner, token:("Close Parentheses",token)),
    (r"\[",lambda scanner, token:("Open Bracket",token)),
    (r"\]",lambda scanner, token:("Close Bracket",token)),
    (r"\{",lambda scanner, token:("Open Curly Brace",token)),
    (r"\}",lambda scanner, token:("Close Curly Brace",token)),
    (r"(\+=|-=|/=|\*=|>>=|<<=|\|=|\&=)", lambda scanner, token:("Assignment Operator",token)),
    (r"(==|>|<|>=|<=|!=|!)", lambda scanner, token:("Comparator",token)),
    (r"=", lambda scanner, token:("Assignment",token)),
    (r"(\+|\-|/|\*|\%)+", lambda scanner, token:("Operation",token)),
    (r"\s+", lambda scanner, token:("Whitespace",token)),
    (r"(,|:|;|\\)", lambda scanner, token:("Punctuation",token)),
    (r"(\&|\||>>|<<|\^=)", lambda scanner, token:("Bit Operation",token))
    ])
    
    return s

def getFileLines(fname):
	with open(fname, encoding="utf-8") as f:
	    content = f.readlines()

	#AVIEL93
	#remove comments and white space
	new_content = []
	for line in content:
		line = line.strip()
		if len(line)>2:
			#cpp
			if fname[-4:]=='.cpp' and line[0] != '/' and line[1] != '/':
				new_content.append(line)
			#python
			if fname[-3:]=='.py' and line[0] != '#' and line[:3] != "'''":
				new_content.append(line)

	return new_content

def levenshtein(s1, s2):
	#https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    d=[]
    s=[]
    ins=[]
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

#AVIEL93
def SmallestLevenshteinPairs(s1,s2):
	pairs=[]
	for s1 in f1sentences:
		p = []
		min_diff=float('Inf')
		for s2 in f2sentences:
			diff = levenshtein(s1,s2)
			if diff < min_diff and diff < min(len(s1),len(s2))/3:
				min_diff = diff
				p = [s1,s2]
		pairs.append(p)
	return pairs

#AVIEL93
def SharedSmallestLevenshteinPairs(s1,s2):
	pairs1=[]
	for s1 in f1sentences:
		p = []
		min_diff=float('Inf')
		for s2 in f2sentences:
			diff = levenshtein(s1,s2)
			if diff < min_diff:
				min_diff = diff
				p = [s1,s2]
		pairs1.append(p)

	#pairs1 from File1 -> File2
	print('File1 -> File2 found ('+str(len(pairs1))+') most simular lines ')

	pairs2=[]
	for s2 in f2sentences:
		p = []
		min_diff=float('Inf')
		for s1 in f1sentences:
			diff = levenshtein(s1,s2)
			if diff < min_diff:
				min_diff = diff
				p = [s2,s1]
		pairs2.append(p)

	#pairs2 from File2 -> File1
	print('File2 -> File1 found ('+str(len(pairs2))+') most simular lines ')

	#CrossCheckedPairs are pairs that are in both pairs1 and pairs2
	sharedPairs = [pair for pair in pairs1 if pair[::-1] in pairs2]

	#Check that pairs are not identical
	pairs_temp = []
	for p in sharedPairs:
		if p[0]!=p[1]:
			pairs_temp.append(p)
	sharedPairs=pairs_temp

	print('Number of shared pairs: '+str(len(sharedPairs)))
	
	return sharedPairs

def getVars(pair):

	'''
	varlist=[]
	for tok in p1:
		if tok[0] == 'String Literal':
			varlist.append(tok[1])
	return varlist
	'''
	#this does the same as above, but leaving it for readablity
	return [pair[1] for pair in pair if pair[0] == 'String Literal']




#AVIEL93
if __name__ == "__main__":

	#get pairs
	pairs=[]
	f1sentences = getFileLines(sys.argv[1])
	f2sentences = getFileLines(sys.argv[2])
	pairs=SharedSmallestLevenshteinPairs(f1sentences,f2sentences)

	#we have to do this for every pair, for now its
	#its easyer to just do one for testing
	testpair = pairs[4]

	#tokenize
	s=init_scanner()
	p1 = s.scan(testpair[0])[0]
	p2 = s.scan(testpair[1])[0]

	#get vars
	vars1 = getVars(p1)
	vars2 = getVars(p2)
	

	#check that have same number of vars
	#if so then we can make the edit pairs
	if len(set(vars1)) == len(set(vars2)):
		#set some kind of mapping of vars to var equivelent
		#ok, now take p1 and p2 and and swap the vars
		#cool now we should have the edit pairs

	#check that edit pair is not the same as original pair
	#how ever if they are we know that they are 
	#semantically (or sytacitcally?) the same

	#make new files with edit pairs

	#run and test?

	





