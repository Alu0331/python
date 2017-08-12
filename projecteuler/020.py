from math import factorial
l = factorial(100)
m = [int(i) for i in str(l)]
print(sum(m))


def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

def test_fact():
    print(fact(10))