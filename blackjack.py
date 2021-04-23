"""
Name: Sally Poon
Student Number: A01232177

This is a module to play BlackJack 21.
"""

"""
========================================================================================================================
                                                CONSTANTS
========================================================================================================================
"""


def BUST_VALUE():
    """Return the Bust limit (at 21).

    :return: an integer, the bust limit.
    """
    pass


def STAND_LIMIT():
    """Return the dealer's stand limit.

    :return: an integer, the dealer's stand limit.
    """
    pass


def CARD_VALUES():
    """Return all the possible card values in a deck excluding joker.

    The key is the face of a card and the value is the actual value of the card in BlackJack

    :return: a dictionary
    """
    pass


def CARD_SUITS():
    """Return all the possible card suits in a deck.

    :return: a tuple
    """
    pass


def MINIMUM_BET():
    """Return the minimum bet amount.

    :return: an integer, the minimum bet amount
    """
    pass


def START_BANK():
    """Return the initial amount for the player's betting balance.

    :return: an integer, the starting amount in player's balance
    """
    pass


"""
========================================================================================================================
                                                      CLASSES
========================================================================================================================
"""


class Card:

    def __init__(self):
        """Instantiate a Card class."""
        pass

    def __str__(self):
        """Return the string when the card is printed.

        :return: a string, the returned string if the card is passed to print
        """
        pass

    def __repr__(self):
        """Return the official string representation of the card.

        :return: a string, the official string representation of this card
        """
        pass


class Deck:

    def __init__(self):
        """Instantiate a Deck class."""
        pass

    def __str__(self):
        """Return the string when the deck is printed.

        :return: a string, the returned string if the deck is passed to print
        """
        pass

    def __repr__(self):
        """Return the official string representation of the deck.

        :return: a string, the official string representation of this deck
        """
        pass


class Player:

    def __init__(self):
        """Instantiate a Player class."""
        pass

    def __str__(self):
        """Return the string when the player is printed.

        :return: a string, the returned string if the player is passed to print
        """
        pass

    def __repr__(self):
        """Return the official string representation of the player.

        :return: a string, the official string representation of this player
        """
        pass


class Bank:

    def __init__(self):
        """Instantiate a Bank class."""
        pass

    def __str__(self):
        """Return the string when the bank is printed.

        :return: a string, the returned string if the bank is passed to print
        """
        pass

    def __repr__(self):
        """Return the official string representation of the bank.

        :return: a string, the official string representation of this bank
        """
        pass


class Report:

    def __init__(self):
        """Instantiate a Card class."""
        pass

    def __str__(self):
        """Return the string when this report is printed.

        :return: a string, the returned string if the report is passed to print
        """
        pass

    def __repr__(self):
        """Return the official string representation of the report.

        :return: a string, the official string representation of this report
        """
        pass

