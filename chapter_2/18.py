class Progression:
    def __init__(self, start=0):
        self._current = start
    
    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current 
            self._advance()
            return answer

    def __iter__(self):
        return self

#    def __getitem__(self, j):
        

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))  


class ArithmeticProgression(Progression):
    def __init__(self, increment, start=0):
        super().init(start)
        self._increment = increment

    def _advance(self):
        self._current += increment

class GeometricProgression(Progression):
    def __init__(self, quota, start=1 ):
        super().__init__(start)
        self._quota = quota

    def _advance(self):
        self._current *= self._quota

class FibonacciProgression(Progression):
    def __init__(self, first=1, second=2):
#        self._current = first
        super().__init__(first)
        self._pre = second - first
        
    def _advance(self):
        temp = self._current
        self._current += self._pre
        self._pre = temp

class Absolution(Progression):
    def __init__(self, first=2, second=200):
       super().__init__(first) 
       self._pre = second + abs(first)

    def _advance(self):
        self._current, self._pre = abs(self._pre-self._current), self._current

class Root(Progression):
    def __init__(self, start=1):
        super().__init__(start)

    def _advance(self):
        self._current = pow(self._current, 1/2)

if __name__ == '__main__':
    t = FibonacciProgression(2, 2)
    t.print_progression(8)
    a = Absolution()
    a.print_progression(10) 
    b = Root(64)
    b.print_progression(7)




























