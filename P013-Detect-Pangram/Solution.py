def is_pangram(s):
    lst = []
    for char in s:
        char = char.lower()
        if ((char>='a' and char<='z') and lst.count(char)==0):
            lst.append(char)
    if len(lst) == 26:
        return True
    return False
