# three no sum

# not done on own
# T:  O( n2 ) S: O( n ) - may be a situation every single number in array.

def threeNumberSum(array, targetSum):

    array.sort()
    triplets = []
    for i in range(0,len(array)-2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentsum = array[i] + array[left] + array[right]
            if currentsum == targetSum:
                triplets.append( [ array[i], array[left], array[right] ])
                left += 1
                right -= 1
            elif currentsum < targetSum:
                left += 1
            else:
                right -= 1
    return triplets




print(threeNumberSum( [-3,1,2,0,5,6] , 0))    # [ [-3,1,2 ] ]