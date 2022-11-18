#!/usr/bin/python3

'''Defines the class Board'''


class Board:
    '''Describes the setting up of the board for the game'''
    def __init__(self):
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]

    def display_board(self):
        '''Prints the board arrangement/setting'''
        print("\n")
        print(" " + self.board[0] + " | " +
              self.board[1] + " | " + self.board[2])
        print("-----------")
        print(" " + self.board[3] + " | " +
              self.board[4] + " | " + self.board[5])
        print("-----------")
        print(" " + self.board[6] + " | " +
              self.board[7] + " | " + self.board[8])

    def new_board(self, position, type):
        '''Updates the position of each player at a particular time

        Args:
            position (int): The position of a player at a particular time
            type (boolean): The boolean returned when a player wins
        '''
        try:
            # if a player selects position n, n-1 index should be updated
            # if the position is not already filled, update the board
            if self.board[position - 1] == " ":
                self.board[position - 1] = type
                return True

            # if the position is already filled, ask user to select another
            position
            else:
                print("Position has been selected. Select another position.")
                return False
        except:
            print("Invalid position! Select another position.")

    def select_winner(self, type):
        '''Returns True if three symbols appear in a row

        Args:
            type (boolean): The boolean returned when a player wins
        '''
        if (self.board[0] == type and self.board[1] == type and
                self.board[2] == type) or \
           (self.board[3] == type and self.board[4] == type and
                   self.board[5] == type) or \
           (self.board[6] == type and self.board[7] == type and
                   self.board[8] == type) or \
           (self.board[0] == type and self.board[3] == type and
                   self.board[6] == type) or \
           (self.board[1] == type and self.board[4] == type and
                   self.board[7] == type) or \
           (self.board[2] == type and self.board[5] == type and
                   self.board[8] == type) or \
           (self.board[0] == type and self.board[4] == type and
                   self.board[8] == type) or \
           (self.board[2] == type and self.board[4] == type and
                   self.board[6] == type):
            return True
        else:
            return False

    def check_draw(self):
        '''Returns True if all fields are selected and there is no winner'''
        if " " not in self.board:
            return True
        else:
            return False
