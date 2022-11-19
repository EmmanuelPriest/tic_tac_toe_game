#!/usr/bin/python3

'''Defines the class Player'''


class Player:
    '''Initializes the class Player

    Args:
        type (boolean): The Boolean returned after each player selction
    '''
    def __init__(self, type):
        self.type = type
        self.name = self.get_name()

    def get_name(self):
        '''Returns the name of each player selected'''
        if self.type == "H":
            name = input("Player selecting H, enter your name: ")
        else:
            name = input("Player selecting O, enter your name: ")
        return name
