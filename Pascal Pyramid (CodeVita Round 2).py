from itertools import permutations

def findAns(c):
    l = len(c)
    if l == 2:
        return c[0]*c[1]
    else:
        d = []
        for i in range(l-1):
            d.append(c[i+1]+c[i])
        return findAns(d)

n = input()
a = sorted(map(int,input().split()))[-6:]
b = permutations(a)
print (max([findAns(i) for i in b]))
