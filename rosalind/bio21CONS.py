
f=open('t.txt','r')
l=f.readlines()
d={}
for i in (l):
    k = i.strip()
    m = list(k)
    if (m[0] == '>'):
        s = k.lstrip('>')
        d[s] = ''
        j = s
    else:
        d[j] += k
for i in d.keys():
    m=d[i]
    k=''.join(x for x in m)
    d[i]=list(k)
x=list(d.values())
#print(x)
"""x=[]
for i in range(len(s)):
    t=list(s[i])
    j=list(t[0])
    x.append(j)"""
q=[]
for i in range(len(x[0])):
    e=[]
    for j in range(len(x)):
        e.append(x[j][i])
    q.append(e)
#print(q)
r={}
str1=''
b=['A','C','G','T']
for i in b:
    r[i]=[]
for i in range(len(q)):
    u=[]
    a=q[i].count('A')
    u.append(a)
    r['A'].append(a)
    c = q[i].count('C')
    u.append(c)
    r['C'].append(c)
    g = q[i].count('G')
    u.append(g)
    r['G'].append(g)
    t = q[i].count('T')
    u.append(t)
    r['T'].append(t)
    m=max(u)
    y=u.index(m)
    str1=str1+b[y]
#print(u)
print(str1)
for i in r.keys():
    print(i,':',(' '.join(str(i) for i in r[i])))
