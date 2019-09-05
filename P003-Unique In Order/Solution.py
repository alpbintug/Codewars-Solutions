def unique_in_order(iterable):
    list1 = []
    for char in iterable:
        if(len(list1)==0):
            list1.append(char)
        elif(list1[len(list1)-1] != char):
            list1.append(char)
    return list1
