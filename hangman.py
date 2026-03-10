# Hangman game
# Author: Muhammad Talal

import random
import string

WORD_LIST = [
    "python",
    "javascript",
    "hangman",
    "development",
    "algorithm",
    "function",
    "variable",
    "programming",
    "challenge",
    "computer",
]


def choose_word(word_list):
    return random.choice(word_list)


def display_hangman(tries):
    # simplified representation without ASCII art
    return f"Tries remaining: {tries}"


def play():
    word = choose_word(WORD_LIST)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_lowercase)
    used_letters = set()  # letters guessed by user

    tries = 6

    print("Welcome to Hangman!")

    # game loop
    while len(word_letters) > 0 and tries > 0:
        print(display_hangman(tries))
        print(f"You have {tries} tries left."
              f" Used letters: {' '.join(sorted(used_letters))}")

        # current word display
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('Good guess!')
            else:
                tries -= 1
                print('Letter is not in the word.')
        elif user_letter in used_letters:
            print('You have already used that letter. Please try again.')
        else:
            print('Invalid character. Please try again. Only a-z letters allowed.')
        print()

    # end of game
    if tries == 0:
        print(display_hangman(tries))
        print(f'Sorry, you lost. The word was "{word}".')
    else:
        print(f'Congratulations! You guessed the word "{word}" correctly!')


if __name__ == '__main__':
    play()
