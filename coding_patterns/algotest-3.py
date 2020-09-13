def patternMatcher(pattern, string):
    # Write your code here.
    str_len = len(string)
    pattern_dict = {"x": 0 , "y": 0}
    newPattern, patternModified = getNewPattern(pattern)

    print(newPattern, patternModified,type(patternModified) , "patternModified")
    pattern_dict, firstYPos = getCountAndFirstYPos(newPattern , pattern_dict)
    xyValues_lst = mainLogic(firstYPos, str_len, newPattern, pattern_dict, string, patternModified)
    return xyValues_lst


def mainLogic(firstYPos, str_len, pattern, pattern_dict, string, patternModified):
    # Assume pos of x as 1 and find y pos using pattern_dict and
    # create a string with the assumption of 1 and check if it matches
    # given input string  ; if matched, assumption is true otherwise
    # increase len of x by 1
    #lenOfX = 1
    if len(pattern) > len(string):
        return []

    if pattern_dict['y'] != 0:
        for lenOfX in range(1, str_len):
            # print(pattern_dict)
            x_cnt = pattern_dict['x']
            y_cnt = pattern_dict['y']

            lenOfY = (str_len - (lenOfX * x_cnt)) / y_cnt
            isValidLenOfY = (lenOfY % 1 == 0) or (lenOfY<0)
            #print(lenOfY)
            if not isValidLenOfY:
                continue

            lenOfY = int(lenOfY)

            # IMPORTANT POINT THAT CAN BE MISSED
            yIdx = firstYPos * lenOfX

            x_part = string[:lenOfX]
            y_part = string[yIdx: yIdx + lenOfY]

            #print(yIdx, firstYPos,  x_part , y_part)
            potential_lst = []
            # for char in pattern:
            #     if char == 'x':
            #         potential_lst.append(x_part)
            #     else:
            #         potential_lst.append(y_part)
            potential_lst = map(lambda char : x_part if char == "x" else y_part, pattern )
            potential_str = "".join(potential_lst)

            print(potential_str)
            if potential_str == string:
                return [ x_part, y_part ] if not patternModified else [ y_part, x_part ]


    else:
        lenOfX = len(string) / pattern_dict['x']
        if lenOfX % 1 == 0:
            lenOfX = int(lenOfX)
            x_part = string[:lenOfX]
            potential_lst = map( lambda  char: x_part , pattern )
            if string == "".join(potential_lst):
                return [x_part , ""] if not patternModified else ["", x_part]

    return []


def getNewPattern(pattern):
    patternModified = False
    newPattern = []
    if pattern[0] == 'x':
        return list(pattern), newPattern
    else:
        # change x to y and y to x
        patternModified = True
        for _, char in enumerate(pattern):
            if char == "x":
                newPattern.append("y")
            else:
                newPattern.append("x")
    #print(type(patternModified))
    return newPattern, patternModified


def getCountAndFirstYPos(pattern , pattern_dict):

    YPosNotSet = True
    firstYPos = None
    for i, char in enumerate(pattern):
        if YPosNotSet and char == 'y':
            firstYPos = i
            YPosNotSet = False
        if char not in pattern_dict:
            pattern_dict[char] = 0
        pattern_dict[char] += 1
    return pattern_dict, firstYPos



print(patternMatcher("xxyxxy" , "gogopowerrangergogopowerranger"))    # [ go , powerranger ]
print(patternMatcher("xxxx" , "testtesttesttest"))       # [ test ]

print(patternMatcher("yxx" , "yomama"))       # [ ["ma", "yo"]]


print(patternMatcher("xxyxxy" , "baddaddoombaddaddoomibaddaddoombaddaddoombaddaddoombaddaddoomibaddaddoomibaddaddoom"))    # ["baddaddoom", "baddaddoomi"]