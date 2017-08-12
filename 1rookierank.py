import sys
from collections import Counter
n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
c = Counter(types)

print(max(c, key=c.get))