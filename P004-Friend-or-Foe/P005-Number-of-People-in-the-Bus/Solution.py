def number(bus_stops):
    val = 0
    for arr in bus_stops:
        val+=arr[0]
        val-=arr[1]
    return val
