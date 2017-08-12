from collections import OrderedDict
n = int(input())
d = OrderedDict()
for i in range(n):
    l = input().split(' ')
    p = int(l[-1]) #takes the cost values of each order
    #print(p)
    name = " ".join(l[:-1]) #an their corresponding names
    if d.get(name):
        d[name] += p #adds the price if same names are found
    else:
        d[name] = p #puts th same value
for i,j in d.items():
        print(i,j)