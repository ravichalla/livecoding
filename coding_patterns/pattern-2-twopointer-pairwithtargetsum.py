

# T: O(N) , S: O(1)
def pair_with_targetsum(arr, target_sum):
    left_ptr = 0
    right_ptr = len(arr)-1

    while left_ptr< len(arr)-1 and right_ptr>0:
        leftno=arr[left_ptr]
        rightno=arr[right_ptr]
        curnt_sum = leftno+rightno
        if curnt_sum == target_sum:
            return [left_ptr,right_ptr]
        elif curnt_sum >target_sum:
            right_ptr-=1
        else:
            left_ptr+=1

    return [-1, -1]


print(pair_with_targetsum([1,2,3,4,6], 6))  # 1,3
print(pair_with_targetsum([2,5,9,11], 11))  # [0,2]




# 4
# 3
# 10 20 14
# 4
# 7 7 7 7
# 5
# 10 90 20 90 10
# 3
# 10 3 10