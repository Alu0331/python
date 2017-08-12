def sum_div(n):
	s = 0
	for i in range(1,n):
		if n % i == 0:
			s += i
	return s

p = sum_div(4)
print(p)