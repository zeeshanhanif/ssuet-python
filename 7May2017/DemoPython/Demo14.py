a = [3,4,56,6,7,78,8]
b = []

for i in a:
    b.append(i * 2)

c =[i*2 for i in a]
d = [i*2 for i in a if i % 2==0]
print(c);
print(d);