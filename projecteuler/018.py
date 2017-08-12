#https://projecteuler.net/problem=18
def tri(num,index):
    for i in range(len(num[index])):
        #print('**')
        #print(num[index])
        #print(max([num[(index+1)][i],num[(index+1)][i+1]]))
        #print(num[index][i])
        num[index][i] += max([num[(index+1)][i], num[(index+1)][i+1]])  #max of bottom row's 2 adjacent indexes
       # print('----')
       # print(num[index][i])
    if len(num[index]) == 1: #if reaches top row return 0
        return num[index][0]
    else:
        return tri(num ,(index - 1)) #goes to the suceeding line


r= []  #list for appending data of every row
f=open('t.txt','r') #file opens
l = f.readlines()
for p in l:
     r.append([int(t) for t in p.rstrip('\n').split()]) #appends each row data in the form of a list into a list [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
ans = tri(r,len(r)-2) #calls the 2nd line from bottom
print(ans)  #checks all possibilities and prints
