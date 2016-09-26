i = raw_input()
j = i.replace(' ', '')
i = j.replace('^', '')
j = i.replace('*', '')
i = j.replace('-', '+-')
j = i.replace('-x', '-1x')
i = j.replace('+x', '+1x')
j = i.replace('x+', 'x1+')
i = j.replace('x-', 'x1-')
j = i.strip("+")
i = j
print i
d = {}
for x in i.split('+'):
    if not 'x' in x:
        continue
    a, p = [v for v in x.split('x') ]
    d[int(p)] = int(a)

s = []
for k in sorted(d.keys()):
    s.append(str(d[k]*k)+'*x^'+str(k-1))
print '+'.join(s).replace('+-', '-').replace('*x^0','')

