'''import math
n = int(input())
small_primes = [2,3,5,7,11,13,17,19]
for i in small_primes:
    i = int(i)
if(n%i == 0):
    print("NO")
else:
    print("Yes")'''

import math
p = int(input())
for i in range(0,p):
    n = int(input())
    if n == 2 or n == 3 or n == 5 or n == 7 or n == 11 or n == 13 or n == 17 or n == 19:
        print("yes")
    elif n%2 == 0 or n%3 == 0 or n%5 == 0  or n%7 == 0 or n%11 == 0 or n%13 == 0 or n%17 == 0 or n%19 == 0 or n<=1:
        print("no")
    else:
        sqr = int(math.sqrt(n)) + 1
        flag = 0 ## prime ##
        for divisor in range(5, sqr,2):
            if n % divisor == 0:
                flag = 1
                break

            if(flag == 1):
                print("no")
            else:
                print("yes")
