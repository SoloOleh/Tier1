words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = {}
for word in words:
    char = word[0]
    if char not in grouped_words:
        grouped_words[char] = []
    grouped_words[char].append(word)
print(grouped_words)

#або
from collections import defaultdict
words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = defaultdict(list)
for word in words:
    char = word[0]
    grouped_words[char].append(word)
print(grouped_words)

