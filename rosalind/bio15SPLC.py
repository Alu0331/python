import re
dic = { 'UUU' : 'F', 'CUU' : 'L', 'AUU' : 'I', 'GUU' : 'V',
      'UUC' : 'F', 'CUC' : 'L', 'AUC' : 'I', 'GUC' : 'V',
      'UUA' : 'L', 'CUA' : 'L', 'AUA' : 'I', 'GUA' : 'V',
      'UUG' : 'L', 'CUG' : 'L', 'AUG' : 'M', 'GUG' : 'V',
      'UCU' : 'S', 'CCU' : 'P', 'ACU' : 'T', 'GCU' : 'A',
      'UCC' : 'S', 'CCC' : 'P', 'ACC' : 'T', 'GCC' : 'A',
      'UCA' : 'S', 'CCA' : 'P', 'ACA' : 'T', 'GCA' : 'A',
      'UCG' : 'S', 'CCG' : 'P', 'ACG' : 'T', 'GCG' : 'A',
      'UAU' : 'Y', 'CAU' : 'H', 'AAU' : 'N', 'GAU' : 'D',
      'UAC' : 'Y', 'CAC' : 'H', 'AAC' : 'N', 'GAC' : 'D',
      'UAA' : 'Stop', 'CAA' : 'Q', 'AAA' : 'K', 'GAA' : 'E',
      'UAG' : 'Stop', 'CAG' : 'Q', 'AAG' : 'K', 'GAG' : 'E',
      'UGU' : 'C', 'CGU' : 'R', 'AGU' : 'S', 'GGU' : 'G',
      'UGC' : 'C', 'CGC' : 'R', 'AGC' : 'S', 'GGC' : 'G',
      'UGA' : 'Stop', 'CGA' : 'R', 'AGA' : 'R', 'GGA' : 'G',
      'UGG' : 'W', 'CGG' : 'R', 'AGG' : 'R', 'GGG' : 'G' }
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
list = list(d.values())
#print(list)
str1 = list[0]
s=str1
for i in range(1,len(list)):
    s = re.sub(list[i],'',s)
t=s.replace("T","U")
final=''
for i in range(0,len(t),3):
    y=t[i:i+3]
    final=final+dic[y]
print(final)
