from collections import defaultdict

document = ["Hello","world","World","new","Hello","new","Hello","Hello","new"]
word_counts = defaultdict(int)

for i in document:
    word_counts[i] +=1;

print(word_counts)

def mysort(word,count):
    return count;

#wc = sorted(word_counts.items(),key=lambda (word, count): count,reverse=True)
#print(wc);