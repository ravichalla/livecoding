# permutation in a string check, compare with pattern


# T: O(N+M ) S: O(M)  m is patt len

def permutation_check_with_string( str, pat):
    max_len = 0
    windowstart=0
    match_count=0
    char_freq={}
    for char in pat:
        if char not in char_freq:
            char_freq[char]=0
        char_freq[char]+=1

    for windowend in range(len(str)):
        right_char = str[windowend]

        if right_char in char_freq:
            char_freq[right_char] -=1
            if char_freq[right_char]==0:
                match_count +=1
        if match_count== len(char_freq):
            return True

        if  windowend >= len(pat)-1:
            left_char= str[windowstart]
            windowstart+=1
            if left_char in char_freq:
                if char_freq[left_char]==0:
                    match_count-=1
                char_freq[left_char] +=1

    return   False

print(permutation_check_with_string( "bcdxabcdy", "bcdyabcdx")) # true
print('Permutation exist: ' + str(permutation_check_with_string("oidbcaf", "abc")))
print('Permutation exist: ' + str(permutation_check_with_string("odicf", "dc")))
print('Permutation exist: ' + str(permutation_check_with_string("bcdxabcdy", "bcdyabcdx")))
print('Permutation exist: ' + str(permutation_check_with_string("aaacb", "abc")))

print('Permutation exist: ' + str(permutation_check_with_string("aaacbeeee", "abcd")))