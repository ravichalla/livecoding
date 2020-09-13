def leftMaxArray(array):

    # leftMax=[0 for x in array]
    # leftmaxno = leftMax[0]
    # for i in range(len(array)):
    #     for j in range(i):
    #         if array[j]>= leftmaxno:
    #             leftmaxno = array[j]
    #             leftMax[i]=  leftmaxno

    leftMax=[0 for x in array]
    leftmaxno = leftMax[0]
    for i in range(len(array)):
        leftMax[i] = leftmaxno
        if array[i]>= leftmaxno:
                leftmaxno = array[i]

    rightMax= [0 for x in array]
    rightmaxno = rightMax[0]
    for i in range(len(array)-1,-1,-1):
        rightMax[i]= rightmaxno
        if array[i]>= rightmaxno:
            rightmaxno = array[i]

    print(leftMax)
    print(rightMax)

    w = 0
    for i in range(len(array)):
        height = array[i]
        minheight = min(leftMax[i], rightMax[i])
        if height < minheight:
            w+= minheight-height

    return w

    # outArr = [None] * len(array)
    # for n in range(1,len(array)):
    #     outArr[n] = array[n]
    #     if array[n]> array[n-1]:
    #         outArr[n]= array[n-1]
    #     if array[n] < array[n-1]:
    #         outArr[n]= array[n]
    # return outArr


print(leftMaxArray([1,8,0,0,5,0,0,10,0,0,1,1,0,3]))