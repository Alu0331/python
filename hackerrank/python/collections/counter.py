import collections
n =int(input())
sh = collections.Counter(map(int,input().split()))
nc = int(input())
income = 0
for i in range(nc):
    s, p = map(int, input().split())
    if sh[s]:
        income += p
        sh[s] -= 1

print (income)