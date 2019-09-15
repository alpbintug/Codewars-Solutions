import math
def productFib(prod):
    lst = [0,1]

    
    while lst[-2] < math.sqrt(prod):
        lst.append(lst[-1]+lst[-2])
    for i in range(len(lst)-1):
        if(lst[i]*lst[i+1]==prod):
            return [lst[i],lst[i+1],True]
        elif(lst[i]*lst[i+1]>prod):
            return [lst[i],lst[i+1],False]
