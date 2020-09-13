# smallest difference

# T: O(nlogn + mlogm ) S: O(1)
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    potentialmindiff = float("inf")
    mindiff = float("inf")

    firstpointer = 0
    secondpointer = 0

    while firstpointer < len(arrayOne) and secondpointer < len(arrayTwo):
        firstno = arrayOne[firstpointer]
        secondno = arrayTwo[secondpointer]
        if  firstno == secondno:
            return [firstno, secondno]

        if firstno < secondno:
            potentialmindiff = secondno-firstno
            firstpointer +=1

        else:
            potentialmindiff = firstno - secondno
            secondpointer += 1
        if potentialmindiff < mindiff:
            mindiff = potentialmindiff
            mindiffpair = [firstno,secondno]
    return mindiffpair


print(smallestDifference( [-1,5,10,20,28,3], [26,134,135,15,17]))  # [28,26]