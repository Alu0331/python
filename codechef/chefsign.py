n=int(input())
for j in range(n):
    s=input()
    i=0
    l=[1]
    k=0    #< < < < < < > > > > > > > > < < < < < < < < < < < < <
    #m=[1]
    while i!=len(s):
        if s[i]=='=':
            l.append(l[-1])
            i=i+1
            print(l[-1])

        elif s[i]=='>':
            if (l[-1]-1)<=0:
                i=0
                k=l[0]+1
                l=[k]
                print("from first")
            else:
                l.append(l[-1]-1)
                i+=1
                print(l[-1])

        else:
            l.append(l[-1]+1)
            i=i+1
            print(l[-1])

    print(max(l))
