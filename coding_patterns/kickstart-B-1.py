# def test_case():
#     cp = []
#     cp_cnt = int(input())
#     cp_lst_string = input()
#     cp = cp_lst_string.split()
#     peak_count = 0
#
#     if int(cp[0]) > int(cp[1]):
#         return 0
#     if int(cp[len(cp) - 1]) > int(cp[len(cp) - 2]):
#         return len(cp) - 1
#     for i in range(1, len(cp) - 1):
#         if int(cp[i]) > int(cp[i - 1]) and int(cp[i]) > int(cp[i + 1]):
#             peak_count += 1
#     return peak_count
#
#
# if __name__ == '__main__':
#
#     t = int(input())
#     for x in range(0, t ):
#         print('Case #{}: {}'.format(x+1,test_case()))


# str_in = input()
#
# for case in range(int(str_in)):
#     _ = input()
#     str_in = input()
#     lst = [int(x) for x in str_in.split()]
#
#     res = 0
#
#     for i in range(1, len(lst) - 1):
#         if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
#             res += 1
#
#     print("Case #{}: {}".format(case + 1, res))
str_in = input()

for case in range(int(str_in)):
    _ = input()
    str_in = input()
    lst = [int(x) for x in str_in.split()]

    res = 0

    for i in range(1, len(lst) - 1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            res += 1

    print("Case #{}: {}".format(case + 1, res))