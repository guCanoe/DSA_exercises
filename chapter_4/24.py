def str2num(d, s):
    r = 0
    for i in range(len(s)):
        r+=d[s[-(i+1)]]*10**i
    return r
    
a, b, c = "pot", "pan", "bib"
letters = list(set(list(a) + list(b) + list(c)))

def sum_puzzle(d):
    mapping = {letters[i] : d[i] for i in range(len(d))}
    if str2num(mapping, a) + str2num(mapping, b) == str2num(mapping, c):
        return True
    else:
        return False


def reange(l, t=[], unseted=set(range(10)) ):
    if not l :
        if sum_puzzle(t):
            print t
    for num in unseted:
        reange(l-1, t+[num], unseted-set([num])) 
        
reange(len(letters))
