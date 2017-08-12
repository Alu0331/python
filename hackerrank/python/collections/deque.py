from collections import deque

d = deque()
for i in range(int(input())):
    l = input().split()
    if l[0] == "append": #if given append appends at l[1]
        d.append(l[1])
    elif l[0] == "appendleft": #appends at lestmost
        d.appendleft(l[1])
    elif l[0] == "pop":
        d.pop()
    elif l[0] == "popleft":
        d.popleft()

for i in d:
    print(i, end=" ")