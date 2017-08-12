import time
start = time.time()
def sieve(n=2000000):
    np = set()
    p = []
    ctr = 0
    for i in range(2, n+1):
        if i not in np:
             p.append(i)
             for j in range(i*i, n+1 , i):
                np.add(j)
                ctr += 1
    print(ctr)
    return p
print(sum(sieve(2000000)))
end = time.time()
print(end-start)


'''
import time
start = time.time()

def sieve(n=2000000):
    np = set()
    p = 2
    ctr = 0
    i=2
    while i< n+1:
        np.add(i)
        i+=2
    for i in range(3, n+1,2):
        if i not in np:
            p=p+i
            for j in range(i*i, n+1 , i):
                np.add(j)
                ctr += 1
    print(ctr)
    return p


print(sieve(2000000))
end = time.time()
print(end-start)
'''