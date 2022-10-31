# Assignment: Assignment 1: Hangman
# Author: Arthur Wei
# Finish Time: 2022-10-05
# Description: hangman.py is a program that plays a hangman game.
# Input: file 'dictionary_short.txt' The user will be prompted to enter the size of the word and the number of lives. The user will also be prompted to enter a letter.
# Output: The program will print the hangman game. It will also print the word with the correct letters filled in. It will also print the letters that have been guessed.

from random import choice, random, randint

# make a dictionary.txt in the same folder where hangman.py is located
dictionary_file = "dictionary-short.txt"

# write all your functions herediff -wB output3 ex3.out


def guess_letter(letters_guessed):
    try:
        letter = input("Please choose a new letter >\n").upper()
        if len(letter) > 1 or letter.isalpha() == False:
            raise Exception
        elif letter in letters_guessed:
            print("\nYou have already chosen this letter.")
            letter = guess_letter(letters_guessed)
        else:
            return letter
    except Exception:
        # print("\nPlease enter a single letter.")
        letter = guess_letter(letters_guessed)
    return letter


def EOGcheck(word, health, letters_guessed):
    if health == 0:
        PrintInterface(word, health, letters_guessed)
        print(f"You lost! The word is {word}!")
        return False
    else:
        for letter in word:
            if letter not in letters_guessed and letter != "-":
                return True
            else:
                continue
        PrintInterface(word, health, letters_guessed)
        print(f"Congratulations!!! You won! The word is {word}!")
        return False


def PrintInterface(word, number_of_lives, letters_guessed):
    print("Letters chosen:", ", ".join(letters_guessed))
    print(f'{"  ".join([letter if letter in letters_guessed or letter == "-" else "__" for letter in word])}   lives: {number_of_lives} {"X" * (lives_remaining - number_of_lives)}{"O" * number_of_lives}')


# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12


def import_dictionary(filename):
    dictionary = {}
    max_size = 12
    try:
        f = open(filename, "rt")
        for line in f:
            line = line.strip()
            if 0 < len(line) < max_size and line:
                dictionary.setdefault(len(line), []).append(line)
            elif len(line) >= max_size:
                dictionary.setdefault(max_size, []).append(line)
        f.close()
    except FileNotFoundError:
        print("The file", filename,
              "does not exist. The program will be terminated.")
        exit()
    return dictionary

# print the dictionary (use only for debugging)


def print_dictionary(dictionary):
    max_size = 12
    print(dictionary)
    # for i in range(1, max_size + 1):
    #     if i in dictionary:
    #         print(i, ": [", dictionary[i], "]")

    #     else:
    #         print(i, ": []")
    # pass

# get options size and lives from the user, use try-except statements for wrong input


def get_game_options():
    try:
        size = int(input(
            "Please choose a size of a word to be guessed [3 - 12, default any size]: \n"))
        if size >= 3 and size <= 12:
            print(f"The word size is set to {size}.")
            size = int(size)

        else:
            raise Exception
    except Exception:
        print("A dictionary word of any size will be chosen.")
        size = randint(3, 12)
    try:
        lives = int(
            input("Please choose a number of lives [1 - 10, default 5]: \n"))
        if lives >= 1 and lives <= 10:
            lives = int(lives)
            print("You have", lives, "lives.")
        else:
            raise Exception
    except Exception:
        print("You have 5 lives.")
        lives = 5
    return (size, lives)


# MAIN

if __name__ == '__main__':

    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)

    # print the dictionary (use only for debugging)
    # remove after debugging the dictionary function import_dictionary

    # print_dictionary(dictionary)

    # print a game introduction

    print("Welcome to the Hangman Game!")

 # START MAIN LOOP (OUTER PROGRAM LOOP)

    while True:

     # set up game options (the word size and number of lives)
        size_of_word, number_of_lives = get_game_options()
        lives_remaining = number_of_lives
        letters_guessed = []

    # select a word from a dictionary (according to the game options)
    # use choice() function that selects an item from a list randomly, for example:
    # mylist = ['apple', 'banana', 'orange', 'strawberry']
    # word = choice(mylist)

        word = choice(dictionary[size_of_word]).upper()
        # word = "T-SHIRT"
        # print(word)

    # START GAME LOOP   (INNER PROGRAM LOOP)

        while True:
            # format and print the game interface:
            # Letters chosen: E, S, P                list of chosen letters
            # __ P P __ E    lives: 4   XOOOO        hidden word and lives
            PrintInterface(word, number_of_lives, letters_guessed)
            # ask the user to guess a letter
            letter = guess_letter(letters_guessed)
    # update the list of chosen letters
            letters_guessed.append(letter)
    # if the letter is correct update the hidden word,
    # else update the number of lives
    # and print interactive messages
            if letter in word:
                print("\nYou guessed right!")
            else:
                print("\nYou guessed wrong, you lost one life.")
                number_of_lives -= 1
    # END GAME LOOP   (INNER PROGRAM LOOP)
    # check if the user guesses the word correctly or lost all lives,
    # if yes finish the game
            if EOGcheck(word, number_of_lives, letters_guessed) == True:
                continue
            else:
                break
    # END MAIN LOOP (OUTER PROGRAM LOOP)
        try:
            play_again = input("Would you like to play again [Y/N]?\n").upper()
            if play_again == "Y":
                continue
            else:
                raise Exception
        except Exception:
            print("Goodbye!")
            exit()

    # ask if the user wants to continue playing,
    # if yes start a new game, otherwise terminate the program
