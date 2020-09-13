# Python program to convert Adjacency matrix
# representation to Adjacency List

from collections import defaultdict


# converts from adjacency matrix to adjacency list
def convert(a):
    # { unknownkey: [] }
    adjDict = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                # { 0: [] }
                adjDict[i].append(j)
    return adjDict


# driver code
a = [[0, 0, 1], [0, 0, 1], [1, 1, 0]]  # adjacency matrix
AdjList = convert(a)
print("Adjacency List:")
# print the adjacency list
for i in AdjList:
    print(i, end="")
    for j in AdjList[i]:
        print(" -> {}".format(j), end="")
    print()