
#Maximum Sum Subarray of Size K (easy)


def maxsumContinuousarray(arr,k):
    windstart = 0
    max = -1
    potmax = -1
    for windEnd in range(len(arr)):
        max += arr[windEnd]
        if windEnd>=(k-1):
            if max >= potmax :
                potmax = max
                potend = windEnd
            max -= arr[windstart]
            windstart += 1
    return arr[potend-(k-1):potend+1],

print(maxsumContinuousarray([2,1,5,1,3,2],3))  # [5,1,3]

print(maxsumContinuousarray([2,2,6,1,2,4], 2)) #[2,6]



#
# def max_sub_array_of_size_k(k, arr):
#   max_sum = 0
#   window_sum = 0
#
#   for i in range(len(arr) - k + 1):
#     window_sum = 0
#     for j in range(i, i+k):
#       window_sum += arr[j]
#     max_sum = max(max_sum, window_sum)
#   return max_sum
#
#
# def main():
#   print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
#   print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))
#
#
# main()
