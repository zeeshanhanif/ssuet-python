list = ["A","B", "C"];

for a in list:
    print(a);

print("-----")
print(len(list));
for i in range(len(list)):
    print(i);
    print(list[i]);

for i, document in enumerate(list):
    print(i,document)


