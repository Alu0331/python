import random
#@profile
def merge(first_part,last_part):
    list_of_first_last = []
    while len(first_part) != 0 and len(last_part) != 0:
        if first_part[0] < last_part[0]:
            list_of_first_last.append(first_part[0])
            first_part.remove(first_part[0])
        else:
            list_of_first_last.append(last_part[0])
            last_part.remove(last_part[0])
    if len(first_part) == 0:
        list_of_first_last += last_part
    else:
        list_of_first_last += first_part
    return list_of_first_last
#@profile
def insertion_sort(n):
    for i in range(1,len(n)):
        val = n[i]
        ind = i-1
        while ind>=0 and val<n[ind]:
            n[ind+1] = n[ind]
            ind = ind-1
        n[ind+1] = val
    return n
#@profile
def tim_sort(a):
    no_of_elements = len(a)          #no of given elements.
    elements = []                # input array
    for i in range(9,257):             # to calculate minrun we use the following logic. here the minrun is the minimum length of runs
        if(no_of_elements%i == 0):        #if less than 8, it gets difficult for merge sort.
            elements.append(i)            #if greater then 256, 5266666666666666666666666666666666666666666666666666666666666dxmore cost for insertion sort.
    #print(elements)        #[10, 20, 25, 50, 100] for no_of_elements=100
    power_list = []
    for i in range(5,9):         #why we took 5 to 9 is thet we do not consider the values under 32. 2power5 is 32 hence.
        power_list.append(pow(2,i))       #if N<64, minrun = N.
    '''for i in power_list:
        print(i)
        if(i<33):
            print(power_list)
            power_list.remove(i)'''
    #print(power_list)            #[32, 64, 128, 256] 2poweri where i goes from 5-9
    for i in range(len(elements)):
            if(elements[0]<32):
                elements.remove(elements[0])
            if(elements[0]>32):
                break
    #print(elements)            # [50, 100]  after removing the numbers which are less than 32.

    dic = {}
    for i in power_list:
        dic[i] = []
    #print(dic)              #{32: [], 64: [], 128: [], 256: []}
    m = 0                         #used to place the elements in their keys in the dict
    p = power_list[m]              #next keys values are stored in p
    for i in dic.keys():
        m = m+1
        if(m<=(len(power_list)-1)):
            p = power_list[m]
            for j in elements:
                if(j<p and j>i):
                    dic[i].append(j)
        else:
            for j in elements:
                if(j>i):
                    dic[i].append(j)
    #print(p) #256 last iteration
    #print(dic)      #{32: [50], 64: [100], 128: [], 256: []}
    h = dic[32]   #the values of key 32 in the dic are copied to h in the form of a list
    minrun = h[0]   #initially we are assuming that it is h[0] later the value is changed according to min value
    min = h[0] - 32   #18 in this case.
    for i in dic.keys():
        #print(i)     #32,64,128,256
        random_list = dic[i]
        #print(random_list)    #[50],[100],[],[]
        for j in random_list:
            if((j-i)>0):
                if((j-i)<min):
                    min = j-i
                    minrun = j
    #print(minrun)    #50, through elemination process
    #print(min)       #18 [50-32]
    runs = no_of_elements//minrun
    #print(runs)    #2 in this case
    i = 0
    runs_final = []
    c=0
    ve=minrun                   #final variable which contains value of minrun
    for j in range(86):
        c=c+1
        sample_list = []
        sample_list = a[i:minrun]
        #print(sample_list)
        runs_final.append(sample_list)
        #print(runs_final)
        i = i+ve
        #print(i)
        minrun=minrun+ve
        #print(i,minrun)
    #print(c)
    #print(runs_final)

    insrt = []
    for i in runs_final:
        m = insertion_sort(i)
        insrt.append(m)
    #print(insrt[len(insrt)-1])
    #print(len(insrt))
    for i in range(0,85):
        #print(j)
        first_part = insrt[i]
        last_part = insrt[i+1]
        v=i+1
        final = merge(first_part,last_part)
        insrt[v] = final
    print(final)
a = []
for i in range(0,100):
    a.append(random.randrange(0,100))
#print(a)
tim_sort(a)
