def up_array(arr):
    if(len(arr)==0):
        return None
    val = 0
    lst = []
    for i in range(len(arr)):
        if(arr[-i-1]<0 or arr[-i-1]>9):
            return None
        val += arr[-i-1]*10**i
    val += 1
    while(val > 0):
        lst.append(val%10)
        val//=10
    return lst[::-1]
    
