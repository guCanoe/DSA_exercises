def rearranges(s):
    if len(s) == 1:
        return s
    elif s[0] % 2:
        return rearranges(s[1:]) + [s[0]]
    else:
        return [s[0]] + rearranges(s[1:])
from random import *        
i = range(10)
shuffle(i)
print rearranges(i)    
