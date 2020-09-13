def longestPalindromicSubstring(string):
    # Write your code here.
    longeststring = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestPalindrome(string, i - 1, i + 1)
        even = getLongestPalindrome(string, i - 1, i)
        longestPalindrome = max(odd, even, key= lambda x: x[1]-x[0])
        longeststring = max(longestPalindrome, longeststring, key= lambda x: x[1]-x[0])
    return string[longeststring[0]:longeststring[1]]


def getLongestPalindrome(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx + 1, rightIdx]


print(longestPalindromicSubstring("abaxyzzyxf"))
print(longestPalindromicSubstring("abcdefghfedcbaa"))