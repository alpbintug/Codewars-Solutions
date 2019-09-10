def series_sum(n):
    f = 0.00
    if(n>0):
        for i in range(n):
            f+=1/(3*i+1)
    return '%.2f' % f
