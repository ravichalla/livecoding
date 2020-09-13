def powerset(array, idx = None):
   # Write your code here.
    if idx == None:
        idx = len(array) - 1
	if idx < 0:
		return [[]]
	ele = array[idx]
	subsets = powerset(array, idx - 1)
	for i in range(len(subsets)):
		subsets.append(subsets[i] + [ele])
	return subsets

print(powerset( [1,2,3]))