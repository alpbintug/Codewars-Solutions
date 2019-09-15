def productFib(prod):
    first = 0
    second = 1
    while(first*second < prod):
        first, second = second, first+second
      
    return [first,second,first*second==prod]
