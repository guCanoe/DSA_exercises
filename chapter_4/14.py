def Hanoi(n, s, m, e):
    if n==1:
        return [[s, e]]
    else:
        t = []
        t+=Hanoi(n-1, s, e, m)
        t+=Hanoi(1, s, m, e)
        t+=Hanoi(n-1, m, s, e)
        return t

t = [range(5, 0, -1), [], []]
for s, e in Hanoi(len(t[0]), 0, 1, 2):
    print t
    t[e].append(t[s].pop())
print t


