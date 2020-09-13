str_in = input()

def solve(strr):

    w=0
    h=0
    depth=[1]
    curr = 1

    for i,s in enumerate(strr):
        if s == "(":
            depth.append(int(strr[i-1]))
            curr= curr* depth[-1]
        if s == ")":
            last = depth.pop()
            curr = curr//last
        if s == "E":
            w += curr
        if s == "W":
            w -= curr
        if s == "N":
            h-=curr
        if s == "S":
            h+=curr
    return w%(10**9), h%(10**9)

for case in range(int(str_in)):
    strr = input()
    w, h = solve(strr)

    print("Case #{}: {} {}".format(case + 1, w + 1, h + 1))

