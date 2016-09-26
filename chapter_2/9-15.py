class Vector:
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        elif isinstance(d, list):
            self._coords = d
        else:
            raise TypeError("wrong value type")

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, v):
        self._coords[j] = v

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        r = Vector(len(self))
        for i in range(len(other)):
            r[i] = self[i] + other[i]
        return r

    def __radd__(self, other):
           return self.__add__(other) 

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        r = Vector(len(self))
        for i in range(len(other)):
            r[i] = self[i] - other[i]
        return r

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            r = Vector(len(self))
            for i in range(len(self)):
                r[i] = other * self[i]
        elif isinstance(other, (Vector, list)):
            if len(self) != len(other):
                raise ValueError("dimensions must agree")
            r = 0
            for i in range(len(other)):
                r += self[i] * other[i]
        else :
            raise TypeError("wrong value type")
        return r

    def __rmul__(self, other):
        return self.__mul__(other)

    def __neg__(self):
        r = Vector(len(self))
        for i in range(len(other)):
            r[i] = -r[i]
        return r

    def __eq__(self, other):
        return self._coords == other._coords
        
    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

if __name__ == '__main__':
    v = Vector([1, 2, 3])
    u = [3, 2, 1]
    print v - u
    print v + u
    print u + v
    print 3 * v
    print v * u
