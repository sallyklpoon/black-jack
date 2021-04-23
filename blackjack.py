"""
Name: Sally Poon
Student Number: A01232177

This is a module to play BlackJack 21.
"""

import random

"""
========================================================================================================================
                                                CONSTANTS
========================================================================================================================
"""


def TURN_OPTIONS() -> tuple:
    """Return the player's options available for each turn.

    :return: a tuple,
    """


def GOAL_TOTAL() -> int:
    """Return the goal total hand for the players in the game.

    :return: an integer, the goal total
    """
    return 21


def STAND_LIMIT() -> int:
    """Return the dealer's stand limit

    :return: an integer, the stand limit for a dealer
    """
    return 15


def CARD_VALUES() -> dict:
    """Return all the possible card values in BlackJack 21.

    :return: a dictionary, all the card values
    """
    return {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
            "10": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}


def CARD_SUITS() -> tuple:
    """Return all possible card suits.

    :return: a tuple of card suits
    """
    return "Diamonds", "Hearts", "Clubs", "Spades"


def START_BANK() -> int:
    """Return the starting bank balance for the player.

    :return: an integer, the starting bank balance for a player
    """
    return 100


def MINIMUM_BET() -> int:
    """Return the minimum bet value.

    :return: an integer, the minimum bet permitted
    """
    return 10


def WIN_BONUS() -> int:
    """Return the bonus multiplier for a player's win towards their bet amount to collect.

    :return: an integer, the bonus mulitplier for a player's win
    """
    return 2

"""
========================================================================================================================
                                                      CLASSES
========================================================================================================================
"""


class Card:

    def __init__(self, face: str, value: int, suit: str):
        """Instantiate a Card class.

        :param face: a string
        :param value: an integer
        :param suit: a strng
        :precondition: face and suit are strings, representing the face value and the suit of the card
        :precondition: value is an integer, the value of the card in BlackJack 21
        :postcondition: an instance of the Card class is instantiated
        :return: an instance of the Card class

        >>> two_of_spades = Card("2", 2, "Spades")
        >>> two_of_spades.face
        '2'
        >>> two_of_spades.value
        2
        >>> two_of_spades.suit
        'Spades'
        """
        self.face = face
        self.value = value
        self.suit = suit

    def __str__(self):
        """Return the string when the card is printed.

        :return: a string, the returned string if the card is passed to print

        >>> two_of_spades = Card("2", 2, "Spades")
        >>> print(two_of_spades)
        This card is a 2 of Spades with a value of 2.
        """
        return f"This card is a {self.face} of {self.suit} with a value of {self.value}."

    def __repr__(self):
        """Return the official string representation of the card.

        :return: a string, the official string representation of this card

        >>> two_of_spades = Card("2", 2, "Spades")
        >>> two_of_spades
        Card(2, 2, Spades)
        """
        return f"Card({self.face}, {self.value}, {self.suit})"


class CardDeck:

    def __init__(self):
        """Instantiate a CardDeck class.

        :postcondition: an instance of the CardDeck class is created
        :postcondition: the object will have the cards attribute, a list of 52 cards
        :return: an instance of the CardDeck class

        >>> my_deck = CardDeck()
        >>> len(my_deck.cards)
        52
        >>> my_deck.cards #doctest: +NORMALIZE_WHITESPACE
        [Card(2, 2, Diamonds), Card(2, 2, Hearts), Card(2, 2, Clubs), Card(2, 2, Spades),
        Card(3, 3, Diamonds), Card(3, 3, Hearts), Card(3, 3, Clubs), Card(3, 3, Spades),
        Card(4, 4, Diamonds), Card(4, 4, Hearts), Card(4, 4, Clubs), Card(4, 4, Spades),
        Card(5, 5, Diamonds), Card(5, 5, Hearts), Card(5, 5, Clubs), Card(5, 5, Spades),
        Card(6, 6, Diamonds), Card(6, 6, Hearts), Card(6, 6, Clubs), Card(6, 6, Spades),
        Card(7, 7, Diamonds), Card(7, 7, Hearts), Card(7, 7, Clubs), Card(7, 7, Spades),
        Card(8, 8, Diamonds), Card(8, 8, Hearts), Card(8, 8, Clubs), Card(8, 8, Spades),
        Card(9, 9, Diamonds), Card(9, 9, Hearts), Card(9, 9, Clubs), Card(9, 9, Spades),
        Card(10, 10, Diamonds), Card(10, 10, Hearts), Card(10, 10, Clubs), Card(10, 10, Spades),
        Card(Jack, 10, Diamonds), Card(Jack, 10, Hearts), Card(Jack, 10, Clubs), Card(Jack, 10, Spades),
        Card(Queen, 10, Diamonds), Card(Queen, 10, Hearts), Card(Queen, 10, Clubs), Card(Queen, 10, Spades),
        Card(King, 10, Diamonds), Card(King, 10, Hearts), Card(King, 10, Clubs), Card(King, 10, Spades),
        Card(Ace, 11, Diamonds), Card(Ace, 11, Hearts), Card(Ace, 11, Clubs), Card(Ace, 11, Spades)]
        """
        self.cards = [Card(face=card[0], value=card[1], suit=suit)
                      for card in CARD_VALUES().items() for suit in CARD_SUITS()]

    def __str__(self):
        """Return the string when the deck is printed.

        :return: a string, the returned string if the deck is passed to print

        >>> my_deck = CardDeck()
        >>> print(my_deck) #doctest: +NORMALIZE_WHITESPACE
        This deck contains the following cards:
        [Card(2, 2, Diamonds), Card(2, 2, Hearts), Card(2, 2, Clubs), Card(2, 2, Spades),
        Card(3, 3, Diamonds), Card(3, 3, Hearts), Card(3, 3, Clubs), Card(3, 3, Spades),
        Card(4, 4, Diamonds), Card(4, 4, Hearts), Card(4, 4, Clubs), Card(4, 4, Spades),
        Card(5, 5, Diamonds), Card(5, 5, Hearts), Card(5, 5, Clubs), Card(5, 5, Spades),
        Card(6, 6, Diamonds), Card(6, 6, Hearts), Card(6, 6, Clubs), Card(6, 6, Spades),
        Card(7, 7, Diamonds), Card(7, 7, Hearts), Card(7, 7, Clubs), Card(7, 7, Spades),
        Card(8, 8, Diamonds), Card(8, 8, Hearts), Card(8, 8, Clubs), Card(8, 8, Spades),
        Card(9, 9, Diamonds), Card(9, 9, Hearts), Card(9, 9, Clubs), Card(9, 9, Spades),
        Card(10, 10, Diamonds), Card(10, 10, Hearts), Card(10, 10, Clubs), Card(10, 10, Spades),
        Card(Jack, 10, Diamonds), Card(Jack, 10, Hearts), Card(Jack, 10, Clubs), Card(Jack, 10, Spades),
        Card(Queen, 10, Diamonds), Card(Queen, 10, Hearts), Card(Queen, 10, Clubs), Card(Queen, 10, Spades),
        Card(King, 10, Diamonds), Card(King, 10, Hearts), Card(King, 10, Clubs), Card(King, 10, Spades),
        Card(Ace, 11, Diamonds), Card(Ace, 11, Hearts), Card(Ace, 11, Clubs), Card(Ace, 11, Spades)]
        """
        return f"This deck contains the following cards: {self.cards}"

    def __repr__(self):
        """Return the official string representation of the deck.

        :return: a string, the official string representation of this deck

        >>> my_deck = CardDeck()
        >>> my_deck #doctest: +NORMALIZE_WHITESPACE
        Deck([Card(2, 2, Diamonds), Card(2, 2, Hearts), Card(2, 2, Clubs), Card(2, 2, Spades),
        Card(3, 3, Diamonds), Card(3, 3, Hearts), Card(3, 3, Clubs), Card(3, 3, Spades),
        Card(4, 4, Diamonds), Card(4, 4, Hearts), Card(4, 4, Clubs), Card(4, 4, Spades),
        Card(5, 5, Diamonds), Card(5, 5, Hearts), Card(5, 5, Clubs), Card(5, 5, Spades),
        Card(6, 6, Diamonds), Card(6, 6, Hearts), Card(6, 6, Clubs), Card(6, 6, Spades),
        Card(7, 7, Diamonds), Card(7, 7, Hearts), Card(7, 7, Clubs), Card(7, 7, Spades),
        Card(8, 8, Diamonds), Card(8, 8, Hearts), Card(8, 8, Clubs), Card(8, 8, Spades),
        Card(9, 9, Diamonds), Card(9, 9, Hearts), Card(9, 9, Clubs), Card(9, 9, Spades),
        Card(10, 10, Diamonds), Card(10, 10, Hearts), Card(10, 10, Clubs), Card(10, 10, Spades),
        Card(Jack, 10, Diamonds), Card(Jack, 10, Hearts), Card(Jack, 10, Clubs), Card(Jack, 10, Spades),
        Card(Queen, 10, Diamonds), Card(Queen, 10, Hearts), Card(Queen, 10, Clubs), Card(Queen, 10, Spades),
        Card(King, 10, Diamonds), Card(King, 10, Hearts), Card(King, 10, Clubs), Card(King, 10, Spades),
        Card(Ace, 11, Diamonds), Card(Ace, 11, Hearts), Card(Ace, 11, Clubs), Card(Ace, 11, Spades)])
        """
        return f"Deck({self.cards})"

    def shuffle(self):
        """Shuffle the deck randomly.

        :return: None, the deck will be shuffled

        No doctests, uses random module, but used some tests to check changes are made to self.cards

        >>> my_deck = CardDeck()
        >>> original_copy = my_deck.cards.copy()
        >>> my_deck.shuffle()
        >>> my_deck.cards != original_copy
        True
        """
        random.shuffle(self.cards)

    def top_draw(self):
        """Draw the first card at the top of the deck.

        When a card is drawn, it is removed from the deck.

        :postcondition: the first card in the deck is 'drawn', meaning it is popped from the deck's list of cards
                        and returned
        :return: None, the deck will have have one card gone, the top card

        >>> my_deck = CardDeck()
        >>> my_deck.top_draw()
        Card(2, 2, Diamonds)
        >>> my_deck.top_draw()
        Card(2, 2, Hearts)
        >>> my_deck.top_draw()
        Card(2, 2, Clubs)
        """
        top_card = self.cards.pop(0)
        return top_card


class Player:

    def __init__(self, dealer=False):
        """Instantiate a Player class.

        :param dealer: Boolean
        :precondition: the dealer value is False by default, but can be True if the player type being instantiated
                       is the dealer in the game
        :postcondition: instantiates a player at the table with attributes hand, total, dealer, and aceCount
        :postcondition: self.hand is an empty list to hold Card objects
        :postcondition: self.total is the player's current total points based on their hand of cards
        :postcondition self.aceCount will keep track of the number of aces a player has received and not yet
                       used up to save busts
        :postcondition: self.dealer takes dealer input

        >>> chris = Player()
        >>> sally = Player(dealer=True)
        >>> print(f"Chris: {chris.hand}, Sally: {sally.hand}")
        Chris: [], Sally: []
        >>> print(f"Chris: {chris.total}, Sally: {sally.total}")
        Chris: 0, Sally: 0
        >>> print(f"Chris: {chris.aceCount}, Sally: {sally.aceCount}")
        Chris: 0, Sally: 0
        >>> print(f"Chris: {chris.dealer}, Sally: {sally.dealer}")
        Chris: False, Sally: True
        """
        self.hand = []
        self.total = 0
        self.aceCount = 0
        self.dealer = dealer

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
        """Record a loss, win, or top_draw in the report object.

        :param result: a string
        :precondition: result is a string of either "top_draw", "win" or "lose"
        :postcondition: increments record.loss by 1 if result == "lose"
        :postcondition: increments record.win by 1 if result == "win"
        :postcondition: increments record.top_draw by 1 if result == "top_draw"
        :return: None, modifies either record.loss, record.win, or record.top_draw appropriately
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
# -----------------COMMON FUNCTIONS-------------------------------------------------------------------------------------


def draw_card(person, deck, times=1):
    """Update person's hand with a new drawn card a specified number of times.

    :param person: a Player
    :param deck: a CardDeck
    :param times: an integer, default 1
    :precondition: person is an instance of a Player, with the attribute hands, a list of possible Card objects
    :precondition: deck is an instance of a CardDeck with a list of cards available
    :precondition: times is an integer, the number of cards/times a player should top_draw
    :postcondition: the person's hand will have a card added to it based on the card at the top of the deck
    :return: None, deck and person is modified by decrease and increase of a card respectively
    """
    pass


def bust(person):
    """Determine if the person has busted.

    Bust meaning the total points in their hand has hit > BUST_LIMIT()

    :param person: a Player
    :precondition: person is an instance of the Player class
    :postcondition: return True of False if the person has busted
    :postcondition: a player is bust if their total points is > BUST_LIMIT()
    :return: Boolean, True/False if player's total is > BUST_LIMIT()
    """
    pass


def adjust_ace(person):
    """Adjust the person's total score if they have an ace on hand.

    :param person: a Player
    :precondition: person is an instance of the Player class
    :postcondition: the player's total score is adjusted if and only if they have an ace on hand and their current
                    total score exceeds that the BUST_LIMIT()
    :postcondition: should the player meet any of the two conditions for adjustment, the person's score is subtracted
                    by 10 for each ace they have on hand until their total is <= BUST_LIMIT()
    :return: None, the player's total score possibly modified
    """
    pass


# -----------------START GAME-------------------------------------------------------------------------------------------


def start_game():
    """Start the game by producing the necessary components for the game.

    :postcondition: returns the necessary components: user's player, dealer, bank, deck, and report for the game
                    as a tuple
    :return: a tuple of the necessary game components
    """
    pass


# -----------------END GAME---------------------------------------------------------------------------------------------

def end_game():
    """Determine if the game should end.

    Game will end if deck of cards in game has been exhausted or if the player's bank balance is < MINIMUM_BET()

    :postcondition: return True if the game must end (i.e. deck of cards is empty or player's bank balance is <
                    MINIMUM_BET()
    :postcondition: return False if game does not meet end-game requirements and must continue
    :return: a Boolean
    """
    pass

# -----------------PLAY ROUND-------------------------------------------------------------------------------------------


def start_round(player, dealer, deck):
    """Begin the round by having player and dealer draw 2 cards each.

    :param player: a Player
    :param dealer: a Player
    :param deck: a CardDeck
    :precondition: the player and dealer are instances of the Player class
    :precondition: the deck is an instance of the CardDeck class
    :postcondition: the player and dealer receives 2 cards to their hand by drawing from the deck
    :postcondition: the deck will have cards reduced in its deck.cards attribute by at most, 4 cards
    :return: None, player, dealer, and deck attributes likely modified
    """
    pass


def dealer_turn(dealer, deck):
    """Execute the dealer's turn to draw until they hit their STAND_LIMIT(), the deck is exhausted, or they bust.

    :param dealer: a Player
    :param deck: a CardDeck
    :precondition: the dealer is an instance of a Player class
    :precondition: a deck is an instance of a CardDeck class
    :postcondition: the dealer will draw until the card deck is exhausted, they have reached STAND_LIMIT(), or
                    they bust
    :return: None, the dealer's hand and the deck may be modified
    """
    pass


def player_turn(player, deck):
    """Execute the player's turn to draw until player decides to stand, the deck is exhausted, or they bust.

    :param player: a Player
    :param deck: a CardDeck
    :precondition: the player is an instance of a Player class
    :precondition: a deck is an instance of a CardDeck class
    :postcondition: the player will be asked if they would like to draw until the card deck is exhausted, they bust,
                    or player decides to stand
    :return: None, player and deck attributes possibly modified

    No doctests, player input required
    """
    pass


def player_draw():
    """Return if the player wants to draw another card.

    :postcondition: return Boolean True if player wants to draw another card, return Boolean False if player
                    does not want to draw another card
    :return: Boolean
    """
    pass


def play_round(player, dealer, deck):
    """Execute a full round of BlackJack between a player and dealer.

    :param player: a Player
    :param dealer: a Player
    :param deck: a CardDeck
    :precondition: the player and dealer are instances of the Player class
    :precondition: the deck is an instance of the CardDeck class
    :postcondition: the player and dealer's total, hand, and aces attributes possibly modified as well as deck.cards
                    modified based on game play
    :postcondition: the game ends if the dealer's hand is a bust or user decides to stand
    :return: None, dealer, player, and deck likely modified in attributes

    No doctests, user input required
    """
    pass


# -----------------ENDING THE ROUND-------------------------------------------------------------------------------------

def decide_winner(player, dealer):
    """Determine who the winner is based on the total results.

    :param player: a Player
    :param dealer: a Player
    :precondition: the player and dealer are instances of the Player class
    :postcondition: return a draw if both player and dealer's total scores are equal
    :postcondition: return 'player' if the dealer's hand is bust or if player's total is > dealer's total
    :postcondition: return 'dealer' if the player's hand is bust or if dealer's total is > player's total
    :return: a string, either 'draw', 'player' or 'dealer'
    """
    pass


def win_round(bank, report):
    """Make win round modifications to bank and report.

    :param bank: a Bank
    :param report: a Report
    :precondition: bank is an instance of the Bank class
    :precondition: report is an instance of the Report class
    :postcondition: the bank collects winnings from the bet with a WIN_BONUS() multiplier
    :postcondition: the report updates and increments the report.wins by 1
    :return: None, report and bank attributes updated
    """
    pass


def lose_round(report):
    """Make loss round modifications to bank and report.

    :param report: a Report
    :precondition: bank is an instance of the Bank class
    :precondition: report is an instance of the Report class
    :postcondition: the report updates and increments the report.losses by 1
    :return: None, report.loss attribute updated
    """
    pass


def draw_round(bank, report):
    """Make draw round modifications to bank and report.

    :param bank: a Bank
    :param report: a Report
    :precondition: bank is an instance of the Bank class
    :precondition: report is an instance of the Report class
    :postcondition: the bank collects back the bet amount
    :postcondition: the report updates and increments the report.draws by 1
    :return: None, report and bank attributes updated
    """
    pass


def end_round(winner_result, bank, report):
    """End the round appropriately based on the results of the win for a round.

    :param winner_result: a string of either "draw", "player", or "dealer"
    :param bank: a Bank
    :param report: a Report
    :precondition: bank is an instance of the Bank class
    :precondition: report is an instance of the Report class
    :postcondition: the bank and report is appropriately modified based on winner_results by being passed to
                    the correct helper functions for winning, losing, or draws
    :return: None, the bank and report modified based on the winner_result
    """
    pass


def reset(player, dealer):
    """Reset the player and dealer for another round.

    :param player: a Player
    :param dealer: a Player
    :precondition: the player and dealer are instances of the Player class
    :postcondition: the player and dealer's total, hand, and aces attributes are back to 0 or empty, resetting for
                    the next round
    :return: None, player and dealer attributes modified accurately for the next round
    """
    pass


"""
========================================================================================================================
                                                      MAIN FUNCTION
========================================================================================================================
"""


def blackjack():
    """Execute a game of BlackJack.

    :postcondition: the game will continue to run until one card deck is exhausted
                    or player's bank is < MINIMUM_BET()
    :return: None, executes the game to completion
    """
    pass
