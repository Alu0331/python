import time

import math

@profile

def primes(n):

    start = time.time()

    prime1 = [2]

    sn=int(math.sqrt(n))

    for attempt in range(3,sn+1,2):

        if all((attempt % prime != 0 and n%attempt==0) for prime in prime1):

            prime1.append(attempt)

    end = time.time()

    print(end - start)

    return prime1

n=primes(600851475143)

print(max(n))
