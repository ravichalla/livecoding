str_in = input()

def possible(d,lst,start):
    for x in lst:
        start= start + (-start)%x
    if start>d:
        return False
    return True


def solve( d, lst):
    upper = 2**41
    lower=0

    for _ in range(42):
        middle= (upper+lower)//2
        if not possible(d,lst,middle):
            upper=middle
        else:
            lower=middle
    return middle

for case in range(int(str_in)):
    strr = input()
    n, d = [int(x) for x in strr.split()]
    strr = input()
    lst = [int(x) for x in strr.split()]

    res = solve(d, lst)

    print("Case #{}: {}".format(case + 1, res))
