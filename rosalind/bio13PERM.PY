import itertools
n = 6
l = list(itertools.permutations(range(0,n+1)))
l = sorted(l)
print(len(l))
for i in l:
    print(*list(i))
