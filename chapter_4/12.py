def product(m, n):
    if m == 1:
        return n
    else:
        return n+product(m-1, n)

print product(5, 3)
