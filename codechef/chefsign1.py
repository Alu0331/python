import re
n = int(input())
for i in range(0,n):
    s = input()
    eq_count = s.count('=')
    if(eq_count == len(s)):
        print("1")
    else:
        str = s.replace('=','')
        #print(str)
        len1 = len(max(re.findall('(<+<)*',str)))
        len2 = len(max(re.findall('(>+>)*',str)))
        #print(len1)
        #print(len2)
        res = max(len1,len2,1)
        print(res+1)
