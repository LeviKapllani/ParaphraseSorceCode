import os
import sys

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

	#pairs1 from File1 -> File2
	print('File1 -> File2 found ('+str(len(pairs1))+') most simular lines ')

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

	#pairs2 from File2 -> File1
	print('File2 -> File1 found ('+str(len(pairs2))+') most simular lines ')

	#CrossCheckedPairs are pairs that are in both pairs1 and pairs2
	sharedPairs = [pair for pair in pairs1 if pair[::-1] in pairs2]
	print('Number of shared pairs: '+str(len(sharedPairs)))
	

	return sharedPairs

#AVIEL93
if __name__ == "__main__":


	dir1 = []
	for root, dirs, files in os.walk(sys.argv[1]):  
	    for filename in files:
	        dir1.append(str(root)+str(filename))

	dir2 = []
	for root, dirs, files in os.walk(sys.argv[2]):  
	    for filename in files:
	        dir2.append(str(root)+str(filename))

	pairs=[]
	error_files=[]

	for f1 in dir1:
		for f2 in dir2:
			print('compare: '+str(f1)+' to '+str(f2))

			f1sentences = getFileLines(f1)
			f2sentences = getFileLines(f2)
			try:
				newpairs=SharedSmallestLevenshteinPairs(f1sentences,f2sentences)
				pairs+=newpairs
			except:
				print('error with one of the files: '+str(f1)+' or '+str(f2))
				error_files.append(f1)
				error_files.append(f2)

	for p in pairs:
		print('======')
		print('cpp:')
		print(p[0])
		print('python:')
		print(p[1])
		print('======')
	

	
	cppPhraseDic={}
	pyPhraseDic={}
	for phrase in pairs:

		#pair 1
		if phrase[0] in cppPhraseDic:
			cppPhraseDic[phrase[0]]+=1
		else:
			cppPhraseDic[phrase[0]]=1

		#pair 2
		if phrase[1] in pyPhraseDic:
			pyPhraseDic[phrase[1]]+=1
		else:
			pyPhraseDic[phrase[1]]=1

	
	print('cpp phrases:')
	for key,val in cppPhraseDic.items():
		print(val, " => ", key)

	print('python phrases:')
	for key,val in pyPhraseDic.items():
		print(val, " => ", key)
	

