# all anagrams of the pattern in the given string.  - start index


def allAnagramsstartindex(str, pat):

    char_freq={}
    match_count =0
    windstart=0
    for char in pat:
        if char not in char_freq:
            char_freq[char]=0
        char_freq[char]+=1

    index_lst=[]

    for winend in range(len(str)):
        right_char = str[winend]
        if right_char in char_freq:
            char_freq[right_char]-=1
            if char_freq[right_char]==0:
                match_count+=1
        if match_count== len(char_freq):
            index_lst.append(windstart)

        # start sliding
        #if windstart > len(str)-1:
        if winend >= len(pat)-1:
            left_char= str[windstart]
            windstart += 1
            if left_char in char_freq:
                if char_freq[left_char]==0:
                    match_count-=1
                char_freq[left_char]+=1


    return index_lst


print(allAnagramsstartindex("ppqp", "pq"))  # [ 1,2]
print(allAnagramsstartindex("abbcabc", "abc"))
