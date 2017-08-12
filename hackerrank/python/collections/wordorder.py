from collections import OrderedDict
D = OrderedDict()
for i in range(int(input())):
    a = input().strip()
    if a in D:
        D[a] += 1 #adds the count of the word that are  same in the dictionary
    else:
        D[a] = 1 #puts the same value if not
print(len(D)) #prins the no of items left in the dict
for a in D:
    print(D[a], end= ' ') #uses space to seperate