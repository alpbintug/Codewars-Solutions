def find_short(s):
    words = s.split() #split() function on strings returns a list of words
    l = len(words[0]) #We give shortest length the value of the first words so we can compare
    for word in words:
        if (len(word) < l):
            l = len(word)
    return l
