class Range:
    def __init__(self, start=0, stop=None, step=1):
        if stop is None:
            stop = start
            start = 0

        self._s = start
        self._e = stop
        self._p = step
        self._len = max((self._e - self._s + self._p - 1)//self._p, 0)

    def __len__(self):
        return self._len

    def __getitem__(self, j):
        if j >= self._len:
            raise IndexError("sdfsdfsf")
        return self._s + self._p * j

    def __contains__(self, val):
        if val >= self._e:
            return False
        return not (val-self._s)%self._p

    def __str__(self):
        return '[' + ", ".join([str(i) for i in self]) + "]"

if __name__ == "__main__":
    i = Range(8)
    j = Range(0, 8)
    k = Range(0, 8, 1)
    print i
    print j
    print k
    if 2 in Range(10000000):
        print True
    else:
        print False
    if 9999999 in Range(10000000):
        print True
    else :
        print False



