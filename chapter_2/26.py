class ReversedSequenceIterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._k = len(sequence)

    def __next__(self):
        self._k -= 1
        if self._k < 0:
            raise StopIteration()
        else:
            return self._seq[self._k]

    def __iter__():
        return self
