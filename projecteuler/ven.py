def isprime(n):
    if all(n%i!=0 for i in range(2,n)):
        return True
    else:
        return False
def nthprime(n):
    pr=3
    np=1
    while np<10001:
       if isprime(pr):
          pr=pr+2
          np=np+1
    return(pr)
print(nthprime(10001))
