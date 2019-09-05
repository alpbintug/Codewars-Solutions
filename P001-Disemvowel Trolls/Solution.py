def disemvowel(string):
    string2 = ""
    list = ['a', 'e', 'i', 'o', 'u']
    for char in string[::1]:
        if (char.lower() not in list): # Checking if current characters are vowels
            string2+=char # If not, we add them to our string
    return string2
