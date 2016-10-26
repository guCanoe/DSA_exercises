import sys
data = []
t = 0
for k in range(100):
    a = len(data)
    b = sys.getsizeof(data)
    data.append(None)
    t = sys.getsizeof(data)
    if not t == b:
        print 'Length: {0:3d}; size in bytes {1:4d}'.format(a, b)
    

for k in range(100):
    a = len(data)
    b = sys.getsizeof(data)
    data.pop()
    print 'Length: {0:3d}; size in bytes {1:4d}'.format(a, b)
