import sys
a,b,c,d,e = input().strip().split(' ')
numbers = [int(a),int(b),int(c),int(d),int(e)]
total = sum(numbers)
print(total-max(numbers),end=" ")
print(total-min(numbers))