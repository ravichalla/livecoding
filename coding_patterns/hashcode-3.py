import math, itertools

testCases = int(input())


def perfectSubarray(arr, n):
    perfectSubarrayCount = 0
    subsets = [[]]

    for ele in arr:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [ele])
    subsets.remove([])
    #subsets.sort()
    #setsubsets = list(k for k,_ in itertools.groupby(subsets))
    #print(setsubsets)
    for subset in subsets:
        if IsPerfect(sum(subset)):
            print(subset)
            perfectSubarrayCount += 1

    print(subsets)
    return perfectSubarrayCount


def IsPerfect(num):
    sr = math.sqrt(num)
    if sr == int(sr):
        return True
    return False


for testCase in range(1, testCases + 1):
    n = int(input())
    arr = [int(s) for s in input().split(" ")]
    # print(arr)

    print("Case #{}: {}".format(testCase, perfectSubarray(arr, n)))
