from functions import make_scrambled_word, words


def get_answer_input(shuffled_word):
    print(f"Question: {shuffled_word}")
    # get user a guess
    print("Guess what word is hidden?")
    guess = input("Enter the answer or q to see the answer:")
    return guess

def incorrect_answer(word, shuffled_word):
    print('Incorrect.')
    while True:
        print('Do you want to reveal the answer or try again?')
        tryagain_or_reveal = input("Enter r or t: ")
        if tryagain_or_reveal == 'r' or tryagain_or_reveal == 't':
            return tryagain_or_reveal
        print('Invalid input')


def play_one_guess():
    shuffled_word, word = make_scrambled_word(words)
    while True:
        guess = get_answer_input(shuffled_word)
        if guess == word:
            print("You guessed correctly:)")
            break
        elif guess == 'q':
            print(f"The answer is {word}.")
            break
        else:
            tryagain_or_reveal = incorrect_answer(word, shuffled_word)
            if tryagain_or_reveal == 'r':
                print(f"The answer is {word}.")
                break
            else:
                continue


def play_one_round():
    while True:
        play_one_guess()
        more_or_quit = more_round()
        if not more_or_quit:
            break


def more_round():
    print("Do you want to try more or quit?")
    choice = input("Enter m or q: ")
    while not choice == 'm' and not choice == 'q':
        print("Invalid input")
        choice = input("Enter m or q: ")
    if choice == 'm':
        return True
    if choice == 'q':
        print("See you next time:)")

play_one_round()


