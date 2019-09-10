def iq_test(numbers):
    list = numbers.split()
    for i in range(len(list)):
        if(int(list[i-2])%2==0 and int(list[i-1])%2==0 and int(list[i])%2==1):
            return i+1
        elif(int(list[i-2])%2==1 and int(list[i-1])%2==1 and int(list[i])%2==0):
            return i+1
