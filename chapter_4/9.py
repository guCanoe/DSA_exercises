def fin_max_min(seq):
    if len(seq) == 1 :
        return seq[0], seq[0]
    else:
        big, little = fin_max_min(seq[1:])
        t_b = seq[0] if seq[0] > big  else big
        t_l = seq[0] if seq[0] < little else little
        return t_b, t_l
import random    
i = range(10)
random.shuffle(i)
print fin_max_min(i)
