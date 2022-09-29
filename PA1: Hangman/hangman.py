"""    
    
"""


from random import choice, random

print("Welcome to Hangman!")
print(
    "Please choose a size of a word to be guessed [3 – 12, default any size]:")
set_word_size()


def set_word_size():
    word_size = int(input())
    if word_size < 3 or word_size > 12:
        print("Invalid input. Defaulting to random number.")
        word_size = random(3, 12)
    print("Word size is: " + str(word_size))
