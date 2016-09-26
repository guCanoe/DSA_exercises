def subset(s):
    if len(s) == 1:
        return [s]
    else:
        t = subset(s[1:])
        for i in range(len(t)):
            t.append(t[i] + [s[0]]) 
            t.append([s[0]] + t[i]) 
        return t

for x in  subset(range(5)):
    print x

