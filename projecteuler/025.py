import time
start = time.time()
def fib(n):
    fibs = [0,1]
    for i in range(2,n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
ft
for term in range(1,1000):
    val = str(fib(term))
    if len(val) == 1000:
        ft = term
        break
    else:
        continue
print(ft)
end = time.time()
print(end-start)