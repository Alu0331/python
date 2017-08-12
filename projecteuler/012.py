def divs(n, m):
    if m==1:
        return [1]
    if n%m == 0:
        return [m]+ divs(n, m-1)
    return divs(n, m-1)

l = []
n = 7
while (len(l)<100):
    n = (n*(n+1))/2
    m = n
    l = divs(n,m)
    n = n+1
print(n)