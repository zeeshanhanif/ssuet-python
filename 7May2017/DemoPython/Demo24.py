import random
a = list(range(10));

num = random.choice(a)
print(num)

n = []
for i in range(4):
    n.append(random.choice(a))
print(n);

n1 = [random.choice(a) for _ in range(4)]
print(n1)
