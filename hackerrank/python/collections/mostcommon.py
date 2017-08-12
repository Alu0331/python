from collections import Counter
a = Counter(input())
a = sorted(a.items()) #[('a', 12), ('b', 24), ('c', 18), ('d', 19), ('e', 18)]
#print(a)
a = sorted(a, key=lambda x: x[1], reverse=True)  #  descending order for the values of keys
for i in range(3):
    print(a[i][0], a[i][1])