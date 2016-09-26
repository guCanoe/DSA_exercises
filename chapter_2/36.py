import random

class Creature:
    def __init__(self, name, gender):
        self._name = name
        self._move = None
        self._gender = gender
        self._strength = strength

    def get_name(self):
        return self._name

    def get_strength(self):
        return self._strength

    def get_gender(self):
        return self._gender
    
    def move(self):
        self._move = random.choice([-1, 0, 1])
        return self._move
    
    def get_move(self):
        return self._move

river = [ 0 for x in range(100) ]

for j in range(len(river)):
    b = random.choice(['Bear', 'Fish', None])
    if b:
        river[j] = Creature(b)
    else:
        river[j] = b

"""1. """
p = [] 
for j in range(len(river)):
    if river[j]:
        p.append(river[j].move())
    else:
        p.append(0)
print p
#for t in range(10000):
    
#    for j in range(len(river)):
        
    
