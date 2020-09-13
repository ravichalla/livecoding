def levenshteinDistance(str1, str2):
    # Write your code here.
	E = [[x for x in range(len(str1)+1)] for y in range(len(str2)+1)]
	for i in range(1,len(str2)+1):
		E[i][0]= E[i-1][0]+1
	for i in range(1,len(str2)+1):
		for j in range(1,len(str1)+1):
			if str2[i-1] == str1[j-1]:
				E[i][j] = E[i-1][j-1]
			else:
				E[i][j] = 1+ min(E[i-1][j-1], E[i][j-1], E[i][j-1])
	return E[-1][-1]



print(levenshteinDistance("abc","abcx"))

print(levenshteinDistance("abc","yabcx"))

print(levenshteinDistance("algoexpert","algozexpert"))


