from functions import check_word, make_scrambled_word, words, random_word


def play_one_round(words):
    # make a question
    shuffled_word, word = make_scrambled_word(words)
    # get user a guess
    print("Guess what word is hidden?")
    guess = input("Enter the answer or q to see the answer:")
    # check the answer
    validation = check_word(word, guess, shuffled_word)
    return word, shuffled_word, guess, validation

def more_round():
    print("Do you want to try more or quit?")
    choice = input("Enter m or q: ")
    while not choice == 'm' and not choice == 'q':
        print("Invalid input")
        choice = input("Enter m or q: ")
    if choice == 'm':
        word, shuffled_word, guess, validation = play_one_round(words)
        return validation
    if choice == 'q':
        print("See you next time:)")


word, shuffled_word, guess, validation = play_one_round(words)
# wrong answer
while not validation:
    guess = input("Enter the answer or q to see the answer:")
    validation = check_word(word, guess, shuffled_word)

# correct answer
while validation:
    validation = more_round()

