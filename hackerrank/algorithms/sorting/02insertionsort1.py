def insertionsort(ar,m):
    i=m-1
    temp=ar[i]
    while(ar[i-1]>temp and i>0):
        ar[i]=ar[i-1]
        print(' '.join(map(str,ar)))
        i-=1
    ar[i]=temp
    print(' '.join(map(str,ar)))
    return ar

m = int(input())
ar = [int(i) for i in input().split()]
ar=insertionsort(ar,m)