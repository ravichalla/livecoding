# no char repeat  - substring

def norepeatesubstring(str):
    max_len = 0
    windowstart = 0
    char_freq = {}
    for windowend in range(len(str)):
        rightchar = str[windowend]
        if rightchar not in char_freq:
            char_freq[rightchar]=0
        char_freq[rightchar]+=1

    leftchar = str[windowstart]
    while char_freq[leftchar] > 1:
        char_freq[leftchar]-=1
        if char_freq[leftchar]==0:
            del char_freq[leftchar]
        windowstart +=1


    #max_len = max(max_len, windowend- windowstart +1)

    return len(char_freq)


print(norepeatesubstring("aabccbb"))  # 3   abc
print(norepeatesubstring("abbb"))  # 2 ab