# longest subarray with 1's after replace.


# T: O(n) S: O(1)
def longestsubarray1replace( k, arr):

    max_len = 0
    windstart =0
    max_one_count  = 0
    for winend in range(len(arr)):

        right_char = arr[winend]
        if right_char==1:
            max_one_count +=1

        if (winend - windstart + 1 - max_one_count )> k:
            if arr[windstart] == 1 :
                max_one_count -=1
            windstart +=1
        max_len = max( max_len, winend - windstart +1 )
    return max_len



print(longestsubarray1replace( 2, [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1 ] ))

print(longestsubarray1replace( 3,  [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1] ))
