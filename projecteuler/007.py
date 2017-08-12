#to print 10001th prime.
#this code is very optimized for huge numbers.

import time
start = time.time()
def sieve(n=1000000):
    np = set()
    p = []
    ctr = 0
    for i in range(2, n+1):
        if i not in np:
            p.append(i)
            for j in range(i*i, n+1, i):
                np.add(j)
                ctr += 1
    print(ctr)
    return p
print(sieve(105000)[10000])
end = time.time()
print(end-start)
