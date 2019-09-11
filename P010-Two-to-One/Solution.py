def longest(s1, s2):
    return ''.join(sorted(set(s1+s2))) # set function returns the distinct characters from an string, sorted function sorts it, ''.join part joins that value to an empty string and return it.
