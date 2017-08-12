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
    suf = d[i][len(d[i])-3: ]
    for j in d.keys():
        if(j!=i):
            pre = d[j][0:3]
            if(suf == pre):
                print(i,j)
