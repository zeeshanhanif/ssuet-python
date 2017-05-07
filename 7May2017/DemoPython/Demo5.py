from collections import defaultdict

document = ["Hello","World","new","Hello","new"]
word_counts = defaultdict(int)
#word_counts = {};

for i in document:
    word_counts[i] +=1;

print(word_counts)