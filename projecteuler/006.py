import math
import time
start = time.time()
l = [i*i for i in range(101)]
m = [j for j in range(101)]
print(math.pow(sum(m),2)-sum(l))
end = time.time()
print(end-start)

