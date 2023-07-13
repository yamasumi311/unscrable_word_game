import random


def scramble(w):
    # turn string into list letters
    letters = list(w)
    random.shuffle(letters)
    # build scramble_word using letters
    scramble_word = ''
    for i in letters:
        scramble_word = scramble_word + i
    return scramble_word