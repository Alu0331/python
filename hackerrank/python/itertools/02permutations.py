from itertools import permutations
s = input().split()
k = int(s[1])
n = []
l = list(permutations(s[0],k))
for i in l:
    n.append("".join(map(str,i)))
n.sort()
for b in n:
    print(b)