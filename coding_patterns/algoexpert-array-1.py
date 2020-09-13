# # T:O(nlog(n)) , S: O(1)
# def twoNumberSum(array, targetSum):
#     left = 0
#     right = len(array) - 1
#
#     while left < right:
#         firstno = array[left]
#         secondno = array[right]
#         currsum = firstno + secondno
#         if currsum == targetSum:
#             return [firstno, secondno]
#         elif currsum < targetSum:
#             left += 1
#         elif currsum > targetSum:
#             right -= 1
#
#         return [array[left], array[right]]



def twoNumberSum( array, targetSum):
    nums = {}

    for num in array:
        potential_match = targetSum - num
        if potential_match in nums:
            return [num, potential_match]
        else:
            nums[num]= True
    return []


print(twoNumberSum([4,5,3,-1,2], 1))   # [-1,2]