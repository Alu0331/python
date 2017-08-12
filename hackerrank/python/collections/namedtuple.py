'''They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.'''
stu, marks = int(input()), input().split().index("MARKS") #input
print(sum([int(input().split()[marks]) for i in range(stu)]) / stu)
'''the output gets like this
    for every mark the student has attained, it is added up and then divided by the total which gives
    avg '''
 #tried reducing to 2 lines with internet's help
