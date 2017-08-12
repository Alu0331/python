import time
start = time.time()
l = []
for a in range(100,1000):
   for b in range(100,1000):
      if str(a*b) == str(a*b)[::-1]:
         l.append(a*b)
print(max(l))
end = time.time()
print(start-end)
