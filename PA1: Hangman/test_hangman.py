# Author: Arthur Wei
# Finish Time: 2022-10-05
# file: test_hangman.py tests a hangman.py
# input: file 'dictionary_short.txt'
# output: possible assertion errors

from secrets import choice
import hangman
import sys
import io

import string

dictionary_file = 'dictionary-short.txt'

if __name__ == '__main__':

    # test import_dictionary(filename)
    dict_standard = {2: ['ad'],
                     3: ['bat'],
                     4: ['card'],
                     5: ['dress'],
                     6: ['engine'],
                     7: ['T-shirt'],
                     8: ['gasoline'],
                     9: ['gathering'],
                     10: ['evaluation'],
                     11: ['self-esteem'],
                     12: ['unemployment']}
    dictionary = hangman.import_dictionary(dictionary_file)
    # print(dictionary)
    assert dictionary == dict_standard

    # test get_game_options()

    output_standard = 'The word size is set to 4.\nYou have 4 lives.\n'
    hangman.input = lambda x: '4'  # redirect input
    stdout = sys.stdout
    sys.stdout = io.StringIO()   # redirect stdout
    size, lives = hangman.get_game_options()
    output = sys.stdout.getvalue()
    sys.stdout = stdout          # restore stdout
    assert size == 4
    assert lives == 4
    assert output == output_standard

    word = choice(dictionary[size]).upper()
    print(f'The word chosen is {word}')
    guessed_letters = []

    # test PrintInterface()
    hangman.lives_remaining = lives
    hangman.PrintInterface(word, lives, guessed_letters)

    # test guess_letter()
    # Test all incorrect inputs then the correct letter
    inputs = ['1', '%', 'GF', 'A']
    for i in inputs:
        hangman.input = lambda x: i
    stdout = sys.stdout
    sys.stdout = io.StringIO()   # redirect stdout
    letter = hangman.guess_letter(guessed_letters)
    output = sys.stdout.getvalue()
    sys.stdout = stdout          # restore stdout
    assert letter == "A"
    guessed_letters.append(letter)
    inputs = ['V', 'E', 'r', 'd', "C"]  # letters to be inputted
    i = 0

    while True:
        if letter in word:
            print("\nYou guessed right!")
        else:
            print("\nYou guessed wrong, you lost one life.")
            lives -= 1

        hangman.input = lambda x: inputs[i]
        # test PrintInterface() # print interface test
        letter = hangman.guess_letter(guessed_letters)

        guessed_letters.append(letter)
        hangman.PrintInterface(word, lives, guessed_letters)

        assert letter == inputs[i].upper()

        # test EOGcheck() # end of game check
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        End = hangman.EOGcheck(word, lives, guessed_letters)
        output = sys.stdout.getvalue()
        sys.stdout = stdout
        if End != True:
            break
        else:
            i += 1
            continue
    assert End == False

    print('Everything looks good! No assertion errors!')
