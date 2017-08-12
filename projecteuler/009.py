import math
import time
start = time.time()
for b in range(1,500):
    if 1000*(500-b) % (1000-b) == 0:
        a = 1000*(500-b) / (1000-b)
        print(a)
        print(b)
        c = math.sqrt((a*a)+(b*b))
        print(c)
        print(a*b*c)
end = time.time()
print(end-start)
'''solve the 2 equations
aa + bb = c*c

a+b+c = 1000.

You can deduce the following relation

a = (1000*1000-2000*b)/(2000-2b)

or after two simple math transformation, you get:

a = 1000*(500-b) / (1000 - b)'''
