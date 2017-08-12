import math

import time
start= time.time()
l = set()
n = int(input())
d = 2
while n%d == 0:
    l.add(d)
    n = n/2
i = 3
def isprime(n):
    if n<2 or n%2 == 0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i == 0:
            return False
    return True

while i <= n:
    if n%i == 0 and isprime(i):
            while n%i == 0:
                l.add(i)
                n = n/i
    i+=2
print(max(l))
end = time.time()
print(end-start)
