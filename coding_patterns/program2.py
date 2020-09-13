#T: O(n^2 * n!) S: O(n * n!)
#space complexity: n! permutations each of lenght n; space
#time complexity: we have each branch of len n and there will be  n! calls to get to them -
#n recursive calls and apart from slicing happening which is of n,
def getPermutations(array):
    permutations = []
    permutationHelper( array, [], permutations)
    return permutations

def permutationHelper(array, currentPermutation, permutations):
    # recursion base case
    if not len(array)  and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i+1:]
            newPermutation = currentPermutation + [array[i]]
            permutationHelper(newArray, newPermutation, permutations)



print(getPermutations([1,2,3]))