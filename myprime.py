import cProfile
import time
list = [i for i in range(2,400)]
start = time.time()
for i in list:
    for a in list:
            if a!=i and a%i == 0:
                list.remove(a)
print(list)
end = time.time()
print(end-start)
