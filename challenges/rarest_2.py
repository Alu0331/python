import collections
f=open('t.txt','r')
l=f.readlines()
#print(l)
l1 = ""
for line in range(0, len(l) - 1):
    l1 = l1 + l[line]
l2 = collections.Counter(l1)
print(l2)
