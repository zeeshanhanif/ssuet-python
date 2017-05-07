from collections import Counter

document = ["Hello","world","World","new","Hello","new","Hello","Hello","new"]

c = Counter(document)
print(c);
print("----");
for word, count in c.most_common(2):
    print(word)
    print(count)

