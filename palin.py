def reverse(n):
    rev = 0
    while(n > 0):
        rem = n %10
        rev = (rev *10) + rem
        n = n//10
    return rev

def palin(n):
    iterations = 0
    s = str(n)
    while (iterations < 5):
        n=n+reverse(n)
        print(n)
        if s[:1]==s[-1:][::-1]:
            print(n)
            return True
        iterations+=1
        break
    return False
n = int(input())
a = palin(n)
print(a)
