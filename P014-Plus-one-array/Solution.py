def up_array(arr):
    if(len(arr)==0):#If array has 0 length, it needs to return None, if we don't check this, it will return 1
        return None
    val = 0
    lst = []
    for i in range(len(arr)):
        if(arr[-i-1]<0 or arr[-i-1]>9):
            return None
        val += arr[-i-1]*10**i
    val += 1
    while(val > 0): #Creating new array in a reversed order, because it is easier to do.
        lst.append(val%10)
        val//=10
    return lst[::-1] #Returning the reverse of our newly created reversed list so it is normal
    
