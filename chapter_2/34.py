import sys
f = open(sys.argv[1])
d = {}
for x in range(65, 91):
    d[chr(x)] = 0
    d[chr(x+32)] = 0

for l in f:
    for c in l:
        if c in d:
            d[c]+=1
for x in range(65, 91):
    n = d[chr(x)] + d[chr(x+32)]
    print chr(x)+': '+n*'i'



        
        
