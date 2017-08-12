
n, m = 86,16
gen = [1, 1]
def fib(i, j):
    count = 2
    while (count < i):
        if (count < j):
            gen.append(gen[-2] + gen[-1])
        elif (count == j or count == j+1):
            gen.append((gen[-2] + gen[-1]) - 1)
        else:
            gen.append((gen[-2] + gen[-1]) - (gen[-(j+1)]))
        count += 1
    return (gen[-1])
print (fib(86,16))
