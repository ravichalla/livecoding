# Python3 program to sort a string 
# of characters 

# function to print string in 
# sorted order

def sortString(str):
    array = [0 for i in range(255)]
    lst = []
    for char in str:
        idx = ord(char)
        array[idx] += 1


    for ascii_code in range(97, 97 + 25):
        char = chr(ascii_code) # gives exact what char
        char_count = array[ascii_code] # count of char
        #lst = [char for i in range(char_count)]
        for i in range(char_count):
            lst.append(char)


    return "".join(lst)


# Driver Code 
s = "geeksforgeeks"
print(sortString(s))

