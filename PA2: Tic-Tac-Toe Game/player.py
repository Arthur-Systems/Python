# author: Arthur Wei
# date: October 23, 2022
# file: player.py a Python program that implements players for the tic-tac-toe game. It contains the Player class, AI class, MiniMax class, and SmartAI class.
# input: user responses (strings)
# output: interactive text messages
import math
from random import random, choice


class Player:
    def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X

    def get_sign(self):
        # return an instance sign
        return self.sign

    def get_name(self):
        # return an instance name
        return self.name

    def choose(self, board):
        valid_choices = []
        for i in range(board.get_size()):
            for j in range(board.get_size()):
                valid_choices.append(chr(ord('a') + i).upper() + str(j + 1))
        while True:
            print()
            cell = input(
                f'{self.name}, {self.sign}: Enter a cell [A-{chr(ord("a") + (board.get_size() - 1)).upper()}][1-{board.get_size()}]:\n').upper()

            if cell in valid_choices and board:
                if board.isempty(cell):
                    board.set(cell, self.sign)
                    break
                else:
                    print('You did not choose correctly.')
            else:
                print('You did not choose correctly.')


class AI (Player):
    def __init__(self, name, sign, board):
        super().__init__(name, sign)
        self.board = board

    def get_empty_cells(self, board):
        empty_cells = []
        cells = [chr(ord('a') + i).upper() + str(j + 1)
                 for i in range(board.get_size()) for j in range(board.get_size())]
        for cell in cells:
            if board.isempty(cell):
                empty_cells.append(cell)
        return empty_cells

    def choose(self, board):
        valid_choices = []
        for i in range(board.get_size()):
            for j in range(board.get_size()):
                valid_choices.append(chr(ord('a') + i).upper() + str(j + 1))
        while True:
            cell = valid_choices[int(random() * len(valid_choices))]
            if board.isempty(cell):
                board.set(cell, self.sign)
                break


class MiniMax (AI):
    def choose(self, board):
        print(
            f"\n{self.name}, {self.sign}: Enter a cell [A-{chr(ord('a')+(board.get_size() - 1)).upper()}][1-{board.get_size()}]: ")
        cell = MiniMax.minimax(self, board, True, True)
        print(cell)
        board.set(cell, self.sign)

    def minimax(self, board, self_player, start):
        if board.isdone():
            if board.get_winner() == self.sign:
                return 1
            elif board.get_winner() == " ":
                return 0
            else:
                return -1
        value = -math.inf if self_player else math.inf
        Best_Move = None

        if self_player:
            for cell in self.get_empty_cells(board):
                board.set(cell, self.sign)
                score = self.minimax(board, False, False)
                if score > value:
                    value = score
                    Best_Move = cell
                board.set(cell, " ")

        else:
            for cell in self.get_empty_cells(board):
                board.set(cell, "O" if self.sign == "X" else "X")
                score = self.minimax(board, True, False)
                if score < value:
                    value = score
                    Best_Move = cell
                board.set(cell, " ")

        if start:
            return Best_Move
        else:
            return value


class SmartAI(AI):
    def choose(self, board):
        print(
            f"\n{self.name}, {self.sign}: Enter a cell [A-{chr(ord('a') + (board.get_size() - 1)).upper()}][1-{board.get_size()}]:")
        cell = SmartAI.smartAI(self, board)
        print(cell)
        board.set(cell, self.sign)

    def OpponentPosition(self, board):
        Positions = []
        for index, cell in enumerate(board.board):
            if cell != self.sign and cell != " ":
                Positions.append(index)
        return Positions

    def GetValidChoices(self, board):
        valid_choices = []
        for i in range(board.get_size()):
            for j in range(board.get_size()):
                valid_choices.append(chr(ord('a') + i).upper() + str(j + 1))
        return valid_choices

    def smartAI(self, board):
        corners = ["A1", "A3", "C1", "C3"]
        center = ["B2"]
        edges = ["B1", "A2", "B3", "C2"]
        valid_choices = self.GetValidChoices(board)

        if all(x == " " for x in board.board):  # first move
            return choice(corners)  # always play corner on the first move
        else:                       # not first moves
            if len(self.get_empty_cells(board)) > 8:
                for x in self.OpponentPosition(board):
                    if valid_choices[x] in center and board.board[x] == " ":
                        return choice(corners)
                    elif valid_choices[x] in corners or edges and board.board[x] == " ":
                        return center[0]

                for edge in edges:
                    for x in self.OpponentPosition(board):
                        if valid_choices[x] != edge:
                            return choice(edges)
                for empty in valid_choices:
                    if empty in corners:
                        return empty
            else:
                for cell in self.get_empty_cells(board):
                    board.set(cell, "O" if self.sign == "X" else "X")
                    if board.isdone():
                        board.set(cell, " ")
                        return cell
                    else:
                        board.set(cell, self.sign)
                        if board.isdone():
                            board.set(cell, " ")
                            return cell
                        board.set(cell, " ")
                return choice(valid_choices)
