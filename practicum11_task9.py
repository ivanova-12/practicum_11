from collections import Counter
from string import punctuation

def words(sntc: str) -> list:
    """Delete symbols of punctuation"""

    only_words = []
    for word in sntc.split():
        only_words.append(word.lower().strip(punctuation))
    return only_words

snt = input()
text = []
text.extend(words(snt))

while snt != '':
    snt = input()
    text.extend(words(snt))

sorted_text = Counter(text)
sorted_text_end = sorted(sorted_text.items(), key=lambda item: item[1], reverse=True)

for key, value in sorted_text_end:
    print(key)
