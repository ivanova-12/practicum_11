import string

only_words = []

for word in input().split():
    if word.strip(string.punctuation) not in only_words:
        only_words.append(word.strip(string.punctuation))

print(only_words)

