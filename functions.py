import random

words = ['apple', 'banana', 'orange', 'lemon', 'watermelon']

# randomly choose a word from an array
def random_word(words):
    word = random.choice(words)
    return word


def scramble(word):
    # turn string into list letters
    letters = list(word)
    random.shuffle(letters)
    # build scramble_word using letters
    scramble_word = ''
    for i in letters:
        scramble_word = scramble_word + i
    return scramble_word

# make a scrambled word
def make_scrambled_word(words):
    # randomly choose a word from a list of words file
    word = random_word(words)
    # make the word scrambled
    scrambled_word = scramble(word)
    return scrambled_word, word




