#O_of_n_square.py
#bubble sort
from random import randint
import math

def sort(n):
	counter = 0
	for i in range(len(n)):
		for j in range(len(n)-1):
			counter += 1
			if n[i] < n[j]:
				n[i], n[j] = n[j], n[i]
	print(len(n), counter, math.ceil(math.log(len(n), 10)), math.ceil(math.log(counter, 10)))


if __name__ == '__main__':
	for k in range(1,5):
		n = list()
		for i in range(10**k):
			n.append(randint(0,100))
		sort(n)
		print(n)