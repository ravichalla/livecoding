def getPermutations(array):
	perms = []
	permutationHelper(0, array , perms)
	return perms
def permutationHelper(i, array, perms):
	if i== len(array)-1:
		perms.append(array[:])
	else:
		for j in range(i, len(array)):
			swap(array, i , j)
			permutationHelper(i+1, array, perms)
			swap(array, i, j)
def swap(array, i, j):
	array[i], array[j] = array[j], array[i]