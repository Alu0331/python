import re
def check_start_end(str):
    if str.startswith('{'):
        if str.endswith('}'):
            return True
    else:
        return True

def  main_func(str):
    len1 = list(re.findall('<{1}',str))
    len2 = list(re.findall('>{1}',str))
    if(len(len1) == len(len2) == 1):
        return True
    else:
        return False

def user_def(str):
    user1 = list(re.findall("\(",str))
    user2 = list(re.findall("\)",str))
    if(len(user1) == len(user2)):
        if(len(user1)!=0):
            t=user_def1(str)
            if(t==True):
                str1=str
                n=0
                for i in range(len(user1)):
                    ind1=str1.index('(')
                    ind2=str1.index(')')
                    ins=instr(str[ind1+1+n:ind2+n])
                    #print("ins",str[ind1+1+n:ind2+n])
                    str1=str[ind2+1:]
                    n=ind2+1
                    #print(str1,ins)
                    if(ins==False):
                        return False
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def user_def1(str):
    try:
        ind1=str.index('<')
        ind2=str.index('>')
        str1=str[ind1+1:ind2]
        u1 = list(re.findall("\(",str1))
        u2 = list(re.findall("\)",str1))
        if re.search('<\(',str) or re.search('\(\(',str) or re.search('\)>',str) or re.search('\)\)',str):
            return False
        elif(len(u1)!=0 or len(u2)!=0):
            return False
        else:
            return True
    except Exception as e:
        pass
def loops(str):
    if str.startswith('{') and str.endswith('}'):
        str = str[1:-1]
    lo1 = list(re.findall('{',str))
    lo2 = list(re.findall('}',str))
    if(len(lo1) == len(lo2) == 0):
        return True
    elif re.search('>[a-zA-Z0-9]*{',str) or re.search('}[a-zA-Z0-9]*\(',str):
        return False
    elif(len(lo1)!=len(lo2)):
        return False
    elif re.search('<{',str) or re.search('\({',str) or re.search('}\)',str) or re.search('}>',str) or re.search('\([a-zA-Z0-9]*{[a-zA-Z0-9]*}[a-zA-Z0-9]*\)$',str):
        return True
    else:
        return False
def instr(str):
    count = 0
    for char in str:
        if char.isalnum():
            count+=1
    #print(count)
    if count>100:
        return False
    return True

n = int(input())
for i in range(n):
    str = input()
    prog = check_start_end(str)
    if(prog == True and main_func(str) and user_def(str) and loops(str)) :
        print("No Compilation Errors")
    else:
        print("Compilation Errors")
