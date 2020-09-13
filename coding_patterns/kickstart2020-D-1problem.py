

def recordBreaker(visitors, n):
    recordBreaksCount = 0
    previousRecord = 0
    for i in range(n):
        greaterThanPreviousDays = i == 0 or visitors[i] > previousRecord
        greaterThanFollowingDay = i == (n - 1) or visitors[i] > visitors[i + 1]

        if greaterThanPreviousDays and greaterThanFollowingDay:
            recordBreaksCount += 1
        previousRecord = max(previousRecord, visitors[i])
    return recordBreaksCount



print(recordBreaker(  [ 1, 2, 0, 7, 2, 0, 2, 0 ], 8))