n = int(input())
l = []
for i in range(0,n):
    str = input().title().split()
    #print(str)
    s = list(str)
    #print(s)
    l.append(s[-1])
    s.remove(s[-1])
    for k in s:
        for i in range(0,1):
           l.append(k[0])
    h=""
    for i in range(1,len(l)):
        h+=l[i]+'. '
    h+=l[0]
    s = []
    l = []
    print(h)
