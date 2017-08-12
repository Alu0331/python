import re
f=open('4.txt','r')
l=f.readlines()
l1 = ""
for line in range(0, len(l) - 1):
    l1 = l1 + l[line]
#print(l1)

#c = re.findall("[A-Z]{3}([a-z])[A-Z]{3}",l1)
c = re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+",l1)
print(c)
