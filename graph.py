import math
def equation(x):
    y = math.sqrt(1 - math.pow(x,2))
    return y

def mean(big,small):
    mean = (big+small)/2
    return mean

piece, radius = 0, 1
n = int(input())
small = 0
bottom = []
for i in range(0,n):
    piece = float("%.6f" % (piece+(radius/n)))
    bottom.append(piece)
print(bottom)
top = []
for i in bottom:
    a = equation(i)
    top.append(a)
#print(top)
width = bottom[0]
big = radius * width
for i in top:
    big += i * width
    small += i * width
#print(small)
res = mean(big,small)
print(res)
