'''def prob(s1,s2):
    tr = set([('A', 'G'), ('G','A'), ('C','T'), ('T','C')])
    ratio = {True: 0.0, False: 0.0}
    for p in zip(s1,s2):
        print(p[0],p[1])
        if(p[0] != p[1]):
            ratio[p in tr] += 1
    return ratio[True]/ ratio[False]'''



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
l = list(d.values())
a = l[0]
b = l[1]
dic = {'A':1,'G':2,'C':-1,'T':-2}
ition,ersion = 0,0
for i in range(0,len(a)):
    if(dic[a[i]] != dic[b[i]]):
        #print(dic[a[i]],dic[b[i]])
        if(dic[a[i]] * dic[b[i]] > 0):
            ition +=1
            #print(ition)
            #print('---')
        else:
            ersion +=1
            #print(ersion)
print(ition/ersion)
