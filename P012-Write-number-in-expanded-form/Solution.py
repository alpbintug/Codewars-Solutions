def expanded_form(num):
    a = str(num)
    b = ''
    for i in range(len(a)):
        if(a[i] != '0'):
            b+=a[i] + '0'*(len(a)-i-1)
            if(i<len(a)-1):
                b+=' + '
    if(a[-1]=='0'):
        b=b[:len(b)-3]    
    return b
