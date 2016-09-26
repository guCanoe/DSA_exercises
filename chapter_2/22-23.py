from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self):
        
    @abstractmethod
    def __getitem__(self, j):
        
    def __contains__(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for j in range(len(self)):
            if self[j] != other[j]:
                return False
        return True

    def __lt__(self, other):
        tail = len(self) if len(self)<len(other) else len(other)
        for j in range(tail):
            if self[j] == other[j]:
                continue
            else:
                return self[j]<other[j]
        return len(self)<len(other)

    def index(self, val):
        for j in range(len(self)):
            if val == self[j]:
                return j
        raise ValueError("value not found")

    def count(self, val):
        c = 0
        for j in range(len(self)):
            if val == self[j]:
                c+=1
        return c

    
