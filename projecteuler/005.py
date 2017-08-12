import time
start= time.time()
def gcd(x,y):
    while y != 0:
        x, y = y, x%y
    return x

def lcm(x,y):
    lcm = (x*y)// gcd(x,y)
    return lcm
p = reduce(lcm,range(1,21))
print(p)
end = time.time()
print(end-start)
