#Smallest Subarray with a given sum


# T: O(
import math
def smallest_subarray_with_given_sum(s, arr):
    winsum =0
    winstart=0
    min_len= math.inf
    for winEnd in range(len(arr)):
        winsum += arr[winEnd]
        while winsum>=s:
            min_len = min(min_len, winEnd-winstart +1)
            winsum -= arr[winstart]
            winstart +=1
    if winsum==math.inf:
        return 0
    return min_len


print(smallest_subarray_with_given_sum(7, [2,1,5,2,3,2]))  # 2
print(smallest_subarray_with_given_sum(8, [2,1,3,5,8])) #1