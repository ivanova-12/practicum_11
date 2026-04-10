from string import punctuation

leaky_letters = ['a', 'b', 'd', 'e', 'g', 'o', 'p', 'q']


def words(sntc: str) -> list:
    """Delete all symbols of punctuation"""

    only_words = []
    for word in sntc.split():
        for letter in word:
            if letter in punctuation:
                word = word.replace(letter, '', 1)
        only_words.append(word)
    return only_words


def real_count_leaky_letters(snt: str) -> int:
    """Count all leaky letters in string"""

    count_leaky_letters = 0

    for word in words(snt):
        for letter in word:
            if letter in leaky_letters:
                count_leaky_letters += 1
                
    return count_leaky_letters


def count_no_leaky_letters(snt: str) -> int:
    """Count all no leaky letters in string"""

    return sum(len(word) for word in words(snt)) - real_count_leaky_letters(snt)


def words_with_leaky_letters(snt: str) -> list:
    """Find all words with 2 or more leaky letters"""

    words_leaky = []

    for word in snt.split():
        count_letters = 0
        for letter in word:
            if letter in leaky_letters:
                count_letters += 1
        if count_letters >= 2:
            words_leaky.append(word.strip(punctuation))

    return words_leaky


if __name__ == '__main__':
    snt = input()
    print(real_count_leaky_letters(snt), count_no_leaky_letters(snt))
    print(words_with_leaky_letters(snt))

