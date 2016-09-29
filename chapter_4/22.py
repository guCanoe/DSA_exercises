def power(x, n):
    r, t, c, ct = 1, x, 0, 1
    while(c < n):
        r *= t * t
        c += ct * 2
        t  *= t
        ct *= 2
        if c + 2*ct > n:
            t=x
            ct=1
    if c > n:
        return r/x
    else:
        return r

for i in range(30):
    print power(2, i)
    print 2**i
    print 
            
            

