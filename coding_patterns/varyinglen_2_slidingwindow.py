# Longest Substring with K Distinct Characters (medium)


# T: O(n) : S: O(k)- distinct char
def longest_substring_with_k_distinct(str, k):

    char_freq = {}
    windowstart = 0
    max_len= 0
    for windowEnd in range(len(str)):

        rightchar= str[windowEnd]
        if rightchar not in char_freq:
            char_freq[rightchar] = 0
        char_freq[rightchar]+=1

        while len(char_freq) > k :
            left_char = str[windowstart]
            char_freq[left_char] -=1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            windowstart +=1
        max_len = max(max_len, windowEnd-windowstart +1)
    return  max_len



def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
