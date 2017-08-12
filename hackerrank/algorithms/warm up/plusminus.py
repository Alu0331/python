import sys
n = int(input().strip())
arr = [int(i) for i in input().strip().split(' ')]
print(round(len([x for x in arr if x>0])/n,3))
print(round(len([x for x in arr if x<0])/n,3))
print(round(len([x for x in arr if x==0])/n,3))