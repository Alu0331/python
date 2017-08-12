sad_list = []

test_cases = int(input())
for i in range(0,test_cases):
    notr, nod = map(int,input().split())
    for i in range(0,notr):
        di,li,sl = map(int,input().split())
        sad_list.append(sl)
