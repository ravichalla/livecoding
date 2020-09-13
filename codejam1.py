#
# def vestigium(arr_2d):
#
#     repeated_rows =0
#     repeated_cols =0
#     for row in range(len(arr_2d)):
#         tmpset = set()
#         for col in range(len(arr_2d)):
#             if arr_2d[row][col] in tmpset:
#                 repeated_rows +=1
#                 break
#             else:
#                 tmpset.add(arr_2d[row][col])
#     for col in range(len(arr_2d)):
#         tmpset = set()
#         for row in range(len(arr_2d)):
#             if arr_2d[row][col] in tmpset:
#                 repeated_cols+=1
#                 break
#             else:
#                 tmpset.add(arr_2d[row][col])
#     trace=0
#     for col in range(len(arr_2d)):
#         for row in range(len(arr_2d)):
#             if row==col:
#                 trace+= arr_2d[row][col]
#     return trace,repeated_rows ,repeated_cols
#
#
# # '''
# if __name__=='__main__':
#
#     t = int(input())
#     for x in range(t):
#         arr_2d = []
#         repeated_rows = 0
#         repeated_cols = 0
#         matrix_size = int(input())
#         for rowvalue in range(matrix_size):
#             row = [int(s) for s in input().split(" ")]
#             arr_2d.append(row)
#             #print("n m",row)
#
#         trace,repeated_rows ,repeated_cols = vestigium(arr_2d)
#         print('Case #{}: {} {} {}'.format( x +1, trace ,repeated_rows, repeated_cols))


def solve(matrix):
    trace = sum([row[i] for i, row in enumerate(matrix)])

    row_cnt = 0
    for row in matrix:
        if sorted(list(set(row))) != sorted(row):
            row_cnt += 1

    matrix = zip(*matrix)
    print(list(matrix))

    col_cnt = 0
    for row in matrix:
        if sorted(list(set(row))) != sorted(row):
            col_cnt += 1

    return trace, row_cnt, col_cnt


str_input = input()
cases = int(str_input)

for case_num in range(1, cases + 1):
    arr_all = []

    str_input = input()
    nrows = int(str_input)

    matrix = []
    for _ in range(nrows):
        str_input = input()
        matrix.append([int(x) for x in str_input.split()])

    trace, row_cnt, col_cnt = solve(matrix)

    print("Case #{}: {} {} {}".format(case_num, trace, row_cnt, col_cnt))