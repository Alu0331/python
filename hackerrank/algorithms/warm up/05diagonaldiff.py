import sys
n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
z1,z2 = 0,0
for x1 in range(n):
    z1 += a[x1][x1]
for x1 in range(n):
    z2 += a[x1][n-x1-1]

print (abs(z2-z1))