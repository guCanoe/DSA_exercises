def log(d):
    if d < 2:
       return 0 
    else:
        return log(d//2)+1

print log(2000)
