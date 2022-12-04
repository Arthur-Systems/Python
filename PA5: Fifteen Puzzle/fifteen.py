# author: Arthur Wei
# date: December 2, 2022
# file: fifteen.py a python file that creates a fifteen puzzle game
# input: User inputted commands
# output: The game of fifteen with the user's commands

import numpy as np
from random import choice


class Fifteen:
    def __init__(self, size=4):
        self.tiles = np.array(
            [i for i in range(1, size**2)] + [0])  # create the tiles
        self.adj = self.getadjecent(size)

    def getadjecent(self, size):
        adj = {}  # create a dictionary with the adjacent tiles
        for i in range(size**2):
            adj[i] = []
            if i - size >= 0:
                adj[i].append(i - size)
            if i + size < size**2:
                adj[i].append(i + size)
            if i % size != 0:
                adj[i].append(i - 1)
            if (i + 1) % size != 0:
                adj[i].append(i + 1)
        return adj

    def update(self, move):
        index = np.where(self.tiles == 0)[0][0]  # get index of 0
        if self.is_valid_move(move):  # if the move is valid
            for i in self.adj[index]:  # for each adjacent tile
                if self.tiles[i] == move:  # if the tile is the move
                    # swap the tiles
                    self.tiles[index], self.tiles[i] = self.tiles[i], self.tiles[index]
                    break

    def transpose(self, i, j):
        if i == j:
            return i

    def shuffle(self, steps=30):
        index = np.where(self.tiles == 0)[0][0]  # get index of 0
        for i in range(steps):
            move_index = choice(self.adj[index])  # choose a random move
            self.tiles[index], self.tiles[move_index] = self.tiles[move_index], self.tiles[index]
            index = move_index  # update index

    def is_valid_move(self, move):
        empty = np.where(self.tiles == 0)[0][0]  # get index of 0
        for i in self.adj[empty]:
            print(self.tiles[i])
            if self.tiles[i] == move:  # if move is adjacent to 0
                return True
        return False

    def is_solved(self):  # check if the game is solved
        for i in range(len(self.tiles) - 1):
            # if the tile is not in the correct position
            if self.tiles[i] != i + 1:
                return False
        return True

    def draw(self):  # draw the game
        print()
        print(" ", '+---' * 4, '+', sep='')

        for i in range(4):
            print(f' |', end='')
            for j in range(4):
                if self.tiles[i * 4 + j] == 0:
                    print(f'   |', end='')
                elif self.tiles[i * 4 + j] >= 10:
                    print(f' {self.tiles[i * 4 + j]}|', end='')
                else:
                    print(f'{self.tiles[i * 4 + j]:2} |', end='')

            print()
            print(" ", '+---' * 4, '+', sep='')
        print()

    def __str__(self):
        string = ''
        for i in range(4):
            for j in range(4):
                if self.tiles[i * 4 + j] == 0:  # if the tile is 0
                    string += "   "
                else:
                    # add the tile to the string
                    string += f'{self.tiles[i * 4 + j]:2} '
            string += "\n"
        return str(string)


if __name__ == '__main__':

    game = Fifteen()
    print(str(game))
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    print("All tests passed")

    '''You should be able to play the game if you uncomment the code below'''

    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
