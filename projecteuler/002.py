a, b = 0, 1
l = []
while True:
    a, b = b, a+b
    if b >= 4000000:
       break
    if b%2 == 0:
       l.append(b)
print(sum(l))
