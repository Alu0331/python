size = int(input())
array = [int(i) for i in input().split()]

for i in range(1, size):
    temp = array[i]
    index = i - 1
    while index >=0 and temp < array[index]:
        array[index + 1] = array[index]
        index -= 1
    array[index + 1] = temp
print(' '.join([str(i) for i in array]))