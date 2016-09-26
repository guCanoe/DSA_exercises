def unique(seq):
    if len(seq) ==1:
        return True
    else:
        return (not seq[0] in seq[1:]) and unique(seq[1:])
print unique([2, 5, 6, 7, 9 ,1])

