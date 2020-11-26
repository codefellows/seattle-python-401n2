from nltk.corpus import words

word_list = words.words()

candidates = [
    # "a dark and stormy night",
    # "n qnex naq fgbezl avtug",
    # "j mjat jwm bcxavh wrpqc",
    # "call me Ismael",
    # "Billy Pilgrim has become unstuck in time",
    "All happy families are alike; each unhappy family is unhappy in its own way.",
    '"Where\'s Papa going with that ax?" said Fern to her mother as they were setting the table for breakfast.',
]


def count_words(text):

    candidate_words = text.split()

    word_count = 0

    for word in candidate_words:
        if word.lower() in word_list:
            print("english word", word)
            word_count += 1

    return word_count


for phrase in candidates:
    word_count = count_words(phrase)
    print(phrase, word_count / len(phrase.split()))
