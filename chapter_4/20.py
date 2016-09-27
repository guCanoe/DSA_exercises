def reang(s, k):
    if len(s) == 1:
        return s
    elif s[0]<k:
        return [s[0]] + reang(s[1:], k)
    else:
        return reang(s[1:], k) + [s[0]]

i = range(20)
from random import shuffle
shuffle(i)
print reang(i, 10)
