def minNumberOfJumps(array):
    # Write your code here.
    # jumps = [float("inf") for x in array]
    # print(jumps)
    # jumps[0]=0
    # for i in range(1,len(array)):
    #     for j in range(0,i):
    #         if array[j]+j >= i:
    #             jumps[i]= min(jumps[j]+1, jumps[i])
    #             print(jumps)
    # return jumps[-1]

    if len(array) == 1:
        return 0
    jumps = 0
    steps = array[0]
    maxReach = array[0]
    for i in range(1, len(array)-1):
        maxReach = max(maxReach, i+ array[i])
        steps -=1
        if steps ==0:
            jumps +=1
            steps = array[i]
    return jumps+1


print(minNumberOfJumps([3,4,2,1,2,3,7,1,1,1,3]))