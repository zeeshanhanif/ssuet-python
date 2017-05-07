def lazy_range(n):
    i = 0
    b = []
    while i < n:
        b.append(i)
        i += 1
    return b

a = lazy_range(5)
print(a);