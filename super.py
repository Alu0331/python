import math
def super_prime(n):
    l = []
    #print(m)
    for i in range(1,n/2):
        if(n%i == 0):
            l.append(i)
            #print(l)

    sum1 = (sum(l))
    #print(sum1)
    a = isprime(sum1)

def isprime(sum1):
        if sum1 == 2 or sum1 == 3 or sum1 == 5 or sum1 == 7 or sum1 == 11 or sum1 == 13 or sum1 == 17 or sum1 == 19:
            print("YES")
        elif (sum1%2 == 0 or sum1%3 == 0 or sum1%5 == 0  or sum1%7 == 0 or sum1%11 == 0 or sum1%13 == 0 or sum1%17 == 0 or sum1<=1) and (sum1<341550071728321):
            print("NO")
        else:
            sqr = int(math.sqrt(n)) + 1
            flag = 0 ## prime ##
            for divisor in range(21,sqr,2):
                if n % divisor == 0:
                    flag = 1
                    break

            if(flag == 1):
                print("NO")
            else:
                print("YES")


x = int(input())
num = list(map(int,input().split()))
for i in num:
    super_prime(i)
