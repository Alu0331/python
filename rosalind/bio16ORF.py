import re
#calculating the orfs for string
def orf(str1):
    yes=['ATG'] #the start codon
    no=['TAA','TAG','TGA'] #the stop codon
    #print(str1)
    uncom='' #the orf of uncomplemented string
    c=0
    orf=[] #the orfs of uncomplemented string
    orfs=[]#all the orfs
    for j in range(0,3):
        str=str1[j:]
        for i in range(0,len(str),3):
            s=str[i:i+3]
            if(len(s)==3):
                t=s.replace("T","U")
                #print(t,dic[t])
                if(s in yes):
                    uncom=uncom+dic[t]
                    c=1
                if((s in no) and (c==1)):
                    orf.append(uncom)
                    uncom=''
                    c=0
                if((c==1) and (s not in yes)):
                    uncom=uncom+dic[t]
        uncom=''
    for i in orf:
        t=i
        for j in t:
            #print(j,t)
            if(j=='M'):
                a=t.index(j)
                orfs.append(t[a:])
                t=t[a+1:]
    return orfs

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
c=list[0]

#print(list)
#uncomplemented string

#calculating reverse complement1
def complement1(s):
	if(s=='A'):
		g='T'
	elif(s=='T'):
		g='A'
	elif(s=='G'):
		g='C'
	else:
		g='G'
	return g

s=c[::-1]
l=[]
g=[]
for i in s:
    l.append(i)
for j in l:
    g.append(complement1(j))
rc=''.join(i for i in g)
uncomorfs=orf(c)
comorfs=orf(rc)
f=set(uncomorfs + comorfs)
for i in f:
    print(i)
