def fact(n):
    return 1 if(n <= 1) else n * fact(n - 1)

k = 5
n = 7          #AaBb birth is success - 0.25% by any combination of phenotypes.
N=pow(2,k)  #N  refers to the total number of trials  #for 2pow k individuals, k success are to be found for N trails.
h = fact(N)
sum = 0
for i in range(n,pow(2,k)+1):
    t = fact(i)
    #print(t)
    o = fact(N-i)
    #print(o)
    c = h/(t*o)
    sum = sum+ (c * pow(0.25,i) * pow(0.75,N-i))
    print(sum)
print(sum)
