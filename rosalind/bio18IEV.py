given = '18787 17975 17919 18981 17497 18303'
numbers = [int(i) for i in given.split(' ')]
#print(numbers)
da = [0.75*numbers[3],0.5*numbers[4],0*numbers[5]]
#print(da)
for i in range(3):
      da.append(numbers[i])
print(sum(da)*2)
