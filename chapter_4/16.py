def reverse(seq):
    if len(seq)<=1:
        return seq 
    else:
        return seq[-1]+reverse(seq[1:-1])+seq[0]

i = "abcdefg"
print reverse(i)
    
