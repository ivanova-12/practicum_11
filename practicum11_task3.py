import string

only_words = []

for word in input().split():
    only_words.append(word.strip(string.punctuation))

print(only_words)

