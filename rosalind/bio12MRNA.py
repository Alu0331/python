D = { 'UUU' : 'F', 'CUU' : 'L', 'AUU' : 'I', 'GUU' : 'V',
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

#f=open('t.txt','r')
#l = f.readlines()
l='MA'
f = 1
for i in range(1,len(l)):
    letter = l[i]
    c = 0
    for j in D.values():
        if(j==letter):
            c = c+1
    f = f*c
print((f*3)%1000000)
