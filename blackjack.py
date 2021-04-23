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


def WIN_BONUS():
    """Return the extra bonus to multiply bet by if player wins.

    :return: an integer, the bonus to multiply the bet by
    """


def TURN_OPTIONS():
    """Return a player's turn options as a tuple.

    :return: a tuple of strings, the player's turn options
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

    def shuffle(self):
        """Shuffle the deck randomly.

        :return: None, the deck will be shuffled
        """
        pass

    def draw(self):
        """Draw the first card at the top of the deck.

        When a card is drawn, it is removed from the deck.

        :return: None, the deck will have have one card gone, the top card
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

    def deduct(self):
        """Deduct the current bet amount from the bank's balance.

        :postcondition: the bank.balance is deducted the bank.bet amount
        :return: None, the bank.balance modified
        """
        pass

    def collect(self, bonus=1):
        """Collect the bet amount multiplied by a bonus.

        Default value of bonus is 1, meaning no bonus.

        :param bonus: an integer
        :precondition: bonus is the bonus multiplier for the collected bet when a player has won
        :postcondition: the Bank.balance appropriately increments by the bank.bet amount multiplied by the bonus
        :return: None, the Bank.balance is modified
        """
        pass

    def get_bet(self) -> int:
        """Return the user's input bet amount as an integer.

        :precondition: user will only input integers
        :postcondition: the integer of user's input is returned
        :return: an integer, the user's bet

        No doctests, requires user input
        """
        pass

    def valid_bet(self, amount):
        """Verify that a bet is valid.

        Give that MINIMUM_BET <= amount <= bank.balance

        :param amount: an integer
        :precondition: amount is an integer representing the bet amount placed by a player
        :postcondition: accurately verify that MINIMUM_BET <= amount <= bank.balance, returning the Boolean of
                        this statement
        :return: Boolean, whether or not the bet amount is valid
        """
        pass

    def place_bet(self):
        """Allow users to place a valid bet.

        :postcondition: the bet amount that the user has specified is deducted from bank.balance and stored in
                        bank.bet
        :return: None, simply modifies both bank.balance and bank.bet
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

    def update(self, result):
        """Record a loss, win, or draw in the report object.

        :param result: a string
        :precondition: result is a string of either "draw", "win" or "lose"
        :postcondition: increments record.loss by 1 if result == "lose"
        :postcondition: increments record.win by 1 if result == "win"
        :postconditoin: increments record.draw by 1 if result == "draw"
        :return: None, modifies either record.loss, record.win, or record.draw appropriately
        """
        pass

    def rounds(self):
        """Return the number of total rounds played.

        :postcondition: accurately sum up wins, losses, and draws to produce the total number of rounds
        :return: an integer, the sum of all rounds that have been played
        """
        pass



"""
========================================================================================================================
                                                      FUNCTIONS
========================================================================================================================
"""
