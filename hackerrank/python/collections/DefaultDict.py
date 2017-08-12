#The defaultdict tool is a container in the collections class of Python.
#It's similar to the usual dictionary (dict) container,
#but it has one difference: The value fields' data type is specified upon initialization.

from collections import defaultdict
d= defaultdict(list)
n, m= list(map(int, input().split()))

for i in range(1,n+1):
    d[input()].append(str(i)) #appends the first string if satisfies the cond. {'a': ['1', '2', '4'], 'b': ['3', '5']})
#print(d)
for i in range(m):
    a = input()
    if a in d.keys():
        print(' '.join(d[a])) #joinss the values for the similar keys and print with a space delimiter
    else:
        print(-1)