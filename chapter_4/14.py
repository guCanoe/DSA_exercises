def Hanoi(t, ts, s, m, e):
    pre = map(len, t)
    if len(t[s][ts:]) == 1:
        t[e].append(t[s].pop())
        print '####'
        print t
        print '####'
    else:
        Hanoi(t, ts+1, s, e, m) 
        Hanoi(t, ts, s, m, e)
        for i in range(pre[s]-2):
            Hanoi(t, pre[m]+1, m, e, s)
            Hanoi(t, len(t[m])-1, m, s ,e)
            m, s = s, m
        print 
        print t
        print ' '.join([str(x) for x in [m,s,e]])
        print 
        Hanoi(t, len(t[m])-1, m, s, e)

t = [ range(4,0,-1), [], [] ]
print t
Hanoi(t, 0, 0, 1, 2)
