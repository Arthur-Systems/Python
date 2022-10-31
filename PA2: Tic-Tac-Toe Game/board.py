# author: Arthur Wei
# date: October 23, 2022
# file: board.py a Python program that draws a tic-tac-toe board and all pieces on it
# input: None
# output: a tic-tac-toe board based on the given size and checks for winner
class Board:
    def __init__(self):
        self.sign = " "
        self.size = 3   # Any size of the board can be used
        self.board = list(self.sign * self.size**2)
        self.winner = " "

    def get_size(self):
        return self.size

    def get_winner(self):
        return self.winner

    def set(self, cell: str, sign: str):
        valid_choices = []
        for i in range(self.size):
            for j in range(self.size):
                valid_choices.append(chr(ord('a') + i).upper() + str(j + 1))
        index = valid_choices.index(cell)
        split = valid_choices[index].split()[0]
        index = ((int(split[1]) - 1) * 3) + ord(split[0].lower()) - ord('a')
        self.board[index] = sign

    def isempty(self, cell: str) -> bool:
        split = cell.split()[0]
        index = ((int(split[1]) - 1) * 3) + ord(split[0].lower()) - ord('a')
        if self.board[index] == " ":
            return True
        else:
            return False

    def isdone(self):
        done = False
        if all(i != " " for i in self.board):
            self.winner = " "
            done = True
        for rows in range(self.size):
            First_Position = self.board[rows * 3]
            if First_Position != " " and all(First_Position == self.board[rows * 3 + i] for i in range(self.size)):
                done = True
                self.winner = First_Position
                break
        for colum in range(self.size):
            First_Position = self.board[colum]
            if First_Position != " " and all(First_Position == self.board[colum + i * 3] for i in range(self.size)):
                done = True
                self.winner = First_Position
                break
        First_Position = self.board[0]
        if First_Position != " " and all(First_Position == self.board[0 + (i * (self.size + 1))] for i in range(self.size)):
            done = True
            self.winner = First_Position
        First_Position = self.board[self.size - 1]
        if First_Position != " " and all(First_Position == self.board[2 + (i * (self.size - 1))] for i in range(self.size)):
            done = True
            self.winner = First_Position
        return done

    def show(self):
        print()
        for i in range(self.size):
            print("  ", chr(ord('a') + i).upper(), end='')
        print()
        print(" ", '+---' * self.size, '+', sep='')

        for i in range(self.size):
            print(f'{i+1}|', end='')
            for j in range(self.size):
                print(f' {self.board[i *3 +j]} |', end='')
            print()
            print(" ", '+---' * self.size, '+', sep='')
