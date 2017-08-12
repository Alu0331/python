from collections import deque

for i in range(int(input())):
    a, d = input(), deque(map(int, input().split()))

    for j in reversed(sorted(d)):

        if d[-1] == j:
            d.pop()

        elif d[0] == j:
            d.popleft()

        else:
            print('No')
            break
    else:
        print('Yes')