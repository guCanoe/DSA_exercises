class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if k < 0:
           k = self._n + k 
        if 0 <= k < self._n:
            return self._A[k]
        raise IndexError('invaild index')

    def append(self, obj):
        if not self._n < self._capacity:
            self._capacity = self._capacity * 2
            self._B = self._make_array(self._capacity)
            for i in range(self._n):
                self._B[i] = self._A[i]
            self._A = self._B
        self._A[self._n] = obj
        self._n += 1
            
    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def insert(self, k, obj):
        if self._n == self._capacity:
            self._capacity *= 2
            self._B = self._make_array(self._capacity)
            for i in range(k):
                self._B[i] = self._A[i]
            self_.B[k] = obj
            for i in range(k, self._n)
                self._B[i] = self._A[i+1]
            self._A = self._B
            self._n += 1
        else:
            for i in range(self._n, k, -1):
                self._A[i] = self._A[i-1]
            self._A[k] = obj
            
        



