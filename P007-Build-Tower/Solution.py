def tower_builder(n_floors):
    tower = []
    for i in range(n_floors):
        floor = ""
        for j in range((2*(n_floors-1)-i*2)//2):
            floor += ' '
        for j in range(i*2+1):
            floor += '*'
        for j in range((2*(n_floors-1)-i*2)//2):
            floor += ' '
        tower.append(floor)
    return tower
