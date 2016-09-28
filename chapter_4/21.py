def find_sp(s, k, a, b):
    if a>=b:
        return
    sp = s[a] + s[b]
    if sp == k:
        print [s[a], s[b]]
        find_sp(s, k, a+1, b-1)
    elif sp > k: 
        find_sp(s, k, a, b-1)
    else:
        find_sp(s, k, a+1, b)
            

find_sp(range(50), 20, 0, 49)
