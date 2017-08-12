f=open('t.txt','r')
l=f.readlines()
d={}
for i in (l):
    k=i.strip()
    m = list(k)
    if(m[0]=='R'):
        d[k] = []
        j=k
    else:
        d[j].append(k)
p=[]
for i in d.keys():
    m=d[i]
    k=''.join(x for x in m)
    d[i]=list(k)
    l1 = k.count('G')
    l2 = k.count('C')
    l = len(d[i])
    per = ((l1 + l2) / l) * 100
    p.append(per)
m=max(p)
i=p.index(m)
f=list(d.keys())
print(f[i])
print(m)

