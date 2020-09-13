def numberOfWaysToMakeChange(n, denoms):
	ways = [0 for amnt in range(n+1)]
	ways[0] = 1
	for denom in denoms:
		for amnt in range(1, n+1):
			if denom <= amnt:
				ways[amnt] += ways[amnt-denom]
  	return ways[n]


print(numberOfWaysToMakeChange(13,[1,5,10,25]))


