from itertools import combinations_with_replacement
a= input().split()
o= list (combinations_with_replacement(sorted(a[0]),int(a[1])))
for i in range (0,len(o)):
    for j in range(0,int(a[1])):
        print (o[i][j],sep='',end='')
    print('')