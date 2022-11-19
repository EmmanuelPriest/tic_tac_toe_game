#!/usr/bin/python3

'''Defines the class Game'''
from board import Board
from player import Player

class Game:
    '''Initializes the class Game'''
    def __init__(self):
        self.board = Board()

        self.player1 = Player("H")
        self.player2 = Player("D")

        self.first_player = self.player1
        self.second_player = self.player2

    def play(self):
        '''Updating the position of each player either win/lose'''
        while True:

            try:

                message = f"{self.first_player.name},\
                enter the position(1 - 9): "
                position = int(input(message))

                # the new_board() method return True if
                # the user selected position is not already filled
                if self.board.new_board(position, self.first_player.type):
                    self.board.display_board()

                    # checking winner each time after updating the board
                    if self.board.select_winner(self.first_player.type):
                        print(f"{self.first_player.name}, wins! and \
                                {self.second_player.name}, loses")
                        break

                    # checking draw each time after updating the board
                    elif self.board.check_draw():
                        print("Game is a draw!")
                        break

                    # changing first player when board is updated
                    else:
                        if self.first_player == self.player1:
                            self.first_player = self.player2
                        else:
                            self.first_player = self.player1
            except IndexError:
                print("Invalid input! Enter a number between 1 and 9.")
