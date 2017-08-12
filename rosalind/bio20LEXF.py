import itertools
s = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#list = [i for i in s.split(' ')]
#print(list)
iter = list(itertools.product(s,repeat=3))
for i in iter:
    print(''.join(j for j in i))
