
def lcs(strings):
    strings = sorted(strings.split())
    short_string = strings[0]
    other_strings = strings[1:]

    l = len(short_string)
    m = ''
    for i in range(0, l):
        for j in range(l, i + len(m), -1):
            s1 = short_string[i:j]

            matched_all = True
            for s2 in other_strings:
                if s1 not in s2:
                    matched_all = False
                    break

            if matched_all:
                m = s1
                break

    return m


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
s = '\n'.join(map(str,l))
res = lcs(s)
print(res)
#print(s)
