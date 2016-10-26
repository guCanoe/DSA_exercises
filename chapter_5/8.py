from time import time

def ave_pop_time(pos, N):
    data = [None for i in range(N)]
    start = time()
    for n in range(N-1, -1, -1):
        data.pop(int(n*pos))
    end = time()
    return (end - start)*10**6/N

for pos in [0, 0.5, 1]:
    l = [str(ave_pop_time(pos, 10**i))[0:5] for i in range(2,6)]
    print "\t".join(l)

