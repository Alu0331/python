def FASTA():
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
