import sys
import re
import numpy
import itertools

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
			diff = levenshtein(s1,s2)/min(len(s1),len(s2))
			if diff < min_diff:
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
			diff = levenshtein(s1,s2)/min(len(s1),len(s2))
			if diff!=0 and diff < min_diff:
				min_diff = diff
				p = [s1,s2]
		pairs1.append(p)

	pairs2=[]
	for s2 in f2sentences:
		p = []
		min_diff=float('Inf')
		for s1 in f1sentences:
			diff = levenshtein(s1,s2)/min(len(s1),len(s2))
			if diff < min_diff:
				min_diff = diff
				p = [s2,s1]
		pairs2.append(p)

	#pairs1 from File1 -> File2
	print('File1 -> File2 found ('+str(len(pairs1))+') most simular lines ')

	#pairs2 from File2 -> File1
	print('File2 -> File1 found ('+str(len(pairs2))+') most simular lines ')

	#CrossCheckedPairs are pairs that are in both pairs1 and pairs2
	sharedPairs = [pair for pair in pairs1 if pair[::-1] in pairs2]
	print('Number of shared pairs: '+str(len(sharedPairs)))
	

	return sharedPairs


#AVIEL93
if __name__ == "__main__":

	#Load Data
	#from command line 
	#file1 = sys.argv[1]
	#file2 = sys.argv[2]
	#files = [file1, file2]
	
	#files = []
	#for f in range(89):
	#	files.append('OneBigTest/'+str(f)+'.cpp')
	

	
	#files = ['OneBigTest/3.cpp',
	#		'OneBigTest/0.cpp']
	

	pairs=[]
	error_files=[]
	print()
	for f1, f2 in itertools.combinations(sys.argv[1:], 2):
		print(f1,f2)
		f1sentences = getFileLines(f1)
		f2sentences = getFileLines(f2)
		try:
			newpairs=SharedSmallestLevenshteinPairs(f1sentences,f2sentences)
			pairs+=newpairs
		except:
			print('error with one of the files')
			error_files.append(f1)
			error_files.append(f2)

	'''
	with open('pairs.txt', 'w') as f:
		for pair in pairs:
			f.write("%s\n" % pair)

    with open('error_log.txt', 'w') as f:
    	for files in error_files:
    		f.write("%s\n" % files)
    '''

	
	for p in pairs:
		print('======')
		print('Original Line of Sorce Code:')
		print(p[0])
		print('Is Most Similar to:')
		print(p[1])
		print('======')
	

	
	phraseDic={}
	for phrase in pairs:

		#pair 1
		if phrase[0] in phraseDic:
			phraseDic[phrase[0]]+=1
		else:
			phraseDic[phrase[0]]=1

		#pair 2
		if phrase[1] in phraseDic:
			phraseDic[phrase[1]]+=1
		else:
			phraseDic[phrase[1]]=1
	
	for key,val in phraseDic.items():
		print(val, " => ", key)
	


	'''
	for word in l:
		if word in dic:
			dic[word]+=amount
		else:
			dic[word]=amount
	'''
	'''
	f1sentences = getFileLines(file1)
	f2sentences = getFileLines(file2)
	pairs = SharedSmallestLevenshteinPairs(f1sentences,f2sentences)


	for p in pairs:
		print('======')
		print('Original Line of Sorce Code:')
		print(p[0])
		print('Is Most Similar to:')
		print(p[1])
		print('======')
		input()
	'''

