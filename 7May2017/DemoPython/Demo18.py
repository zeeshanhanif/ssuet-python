def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

a = lazy_range(5)

print(a);

for i in lazy_range(7):
    if i == 3:
        break
    print(i)