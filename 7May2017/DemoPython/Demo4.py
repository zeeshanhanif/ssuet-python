from collections import defaultdict

document = ["Hello","World","new","Hello","new"]
#word_counts = defaultdict(int)
word_counts = {};

for i in document:
    if i in word_counts:
        word_counts[i] +=1;
    else:
        word_counts[i] = 1;

print(word_counts)