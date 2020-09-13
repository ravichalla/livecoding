# longest substring with same letters after replacement
# replace no more than  k letters

# O(n) T  s; O(1) -26 char
def longsubstring_with_same_letters(k, str):
    max_letter_repeat_count =0
    max_len = 0
    windstart = 0
    char_freq = {}
    for windend in range(len(str)):
        right_char = str[windend]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] +=1

        max_letter_repeat_count = max( max_letter_repeat_count, char_freq[right_char])
        if ( windend - windstart +1 - max_letter_repeat_count)> k:
            left_char = str[windstart]

            char_freq[left_char]-=1
            windstart +=1
        max_len = max(max_len, windend- windstart +1)
    return  max_len

print(longsubstring_with_same_letters(2, "aabccbb"))
print(longsubstring_with_same_letters(1, "abbcb"))
print(longsubstring_with_same_letters(1, "abccde"))