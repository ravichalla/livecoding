
# no should not repeat,

# T: O(n2) S: O(n2)
def fourNumberSum(array, targetSum):

    allPairSums = {}
    quadraplets = []

    for i in range(len(array)):

        for j in range(i+1, len(array)):

            currSum = array[i] + array[j]
            difference = targetSum - currSum
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    print("Pair", pair)
                    quadraplets.append(  pair + [array[i], array[j]])
        for k in range(0, i):
            currSum = array[i] + array[k]
            difference = targetSum - currSum

            if currSum not in allPairSums:
                allPairSums[currSum] = [[array[i], array[k]]]
            else:
                allPairSums[currSum].append(  [array[i], array[k] ] )
    return  quadraplets



print( fourNumberSum( [7,6,4, -1, 1,2 ], 16))