"""
Name: Sally Poon
Student Number: A01232177

This is a module to play BlackJack 21.
"""

import random
import time

"""
========================================================================================================================
                                                CONSTANTS
========================================================================================================================
"""


def WELCOME() -> str:
    """Return the string for welcome message to the game.

    :return: a string, the welcome message
    """
    return f"Hi! Welcome to the table, let's start your game of BlackJack 21.\n" \
           "In this game, the dealer will draw first until they stand before you have the chance to draw or stand.\n" \
           f"The MINIMUM BET value is {MINIMUM_BET()}"


def TURN_OPTIONS() -> tuple:
    """Return the player's options available for each turn.

    :return: a tuple, the options for a user
    """
    return "Hit me! (Draw another Card)", "Stand (End round, stop drawing)"


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

    :return: an integer, the bonus multiplier for a player's win
    """
    return 2


def ACE_MODIFIER() -> int:
    """Return the total modifier when a user has an Ace.

    :return: an integer, the modifier when a user  has an Ace to adjust their soft hand
    """
    return 10


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
        2 of Spades with a value of 2
        """
        return f"{self.face} of {self.suit} with a value of {self.value}"

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

        >>> some_player = Player()
        >>> print(some_player)
        This player has [] for a current total of 0 and 0 Aces valued at a soft 11. This player is a dealer: False.
        >>> some_dealer = Player(dealer=True)
        >>> print(some_dealer)
        This player has [] for a current total of 0 and 0 Aces valued at a soft 11. This player is a dealer: True.
        """
        return f"This player has {self.hand} for a current total of {self.total} and {self.aceCount} Aces " \
               f"valued at a soft 11. This player is a dealer: {self.dealer}."

    def __repr__(self):
        """Return the official string representation of the player.

        :return: a string, the official string representation of this player

        >>> some_player = Player()
        >>> some_player
        Player([], 0, 0, False)
        >>> some_dealer = Player(dealer=True)
        >>> some_dealer
        Player([], 0, 0, True)
        """
        return f"Player({self.hand}, {self.total}, {self.aceCount}, {self.dealer})"


class Bank:

    def __init__(self):
        """Instantiate a Bank class.

        :postcondition: an object of the Bank class is instantiated with attributes balance and bet
        :postcondition: the balance attribute value is equivalent to START_BANK() constant
        :postcondition: the bet attribute will store a player's bet, starting at 0
        :return: an instance of the Bank class

        >>> my_bank = Bank()
        >>> my_bank.balance == START_BANK()
        True
        >>> my_bank.bet
        0
        """
        self.balance = START_BANK()
        self.bet = 0

    def __str__(self) -> str:
        """Return the string when the bank is printed.

        :return: a string, the returned string if the bank is passed to print

        >>> my_bank = Bank()
        >>> print(my_bank)
        The player's bank has a balance of $100 with a bet of $0 placed.
        """
        return f"The player's bank has a balance of ${self.balance} with a bet of ${self.bet} placed."

    def __repr__(self) -> str:
        """Return the official string representation of the bank.

        :return: a string, the official string representation of this bank

        >>> my_bank = Bank()
        >>> my_bank
        Bank(100, 0)
        """
        return f"Bank({self.balance}, {self.bet})"

    @staticmethod
    def get_bet() -> int:
        """Return the user's input bet amount as an integer.

        :precondition: user will only input integers
        :postcondition: the integer of user's input is returned
        :return: an integer, the user's bet

        No doctests, requires user input
        """
        return int(input("How much money would you like to place? (input an integer): "))

    def valid_bet(self, amount: int) -> bool:
        """Verify that a bet is valid.

        Give that MINIMUM_BET <= amount <= bank.balance

        :param amount: an integer
        :precondition: amount is an integer representing the bet amount placed by a player
        :postcondition: accurately verify that MINIMUM_BET <= amount <= bank.balance, returning the Boolean of
                        this statement
        :return: Boolean, whether or not the bet amount is valid

        >>> my_bank = Bank()
        >>> my_bank.valid_bet(9)
        False
        >>> my_bank.valid_bet(10)
        True
        >>> my_bank.valid_bet(13)
        True
        >>> my_bank.valid_bet(100)
        True
        >>> my_bank.valid_bet(101)
        False
        """
        return MINIMUM_BET() <= amount <= self.balance

    def place_bet(self) -> None:
        """Allow users to place a valid bet.

        :postcondition: the bet amount that the user has specified is deducted from bank.balance and stored in
                        bank.bet
        :return: None, simply modifies both bank.balance and bank.bet

        No doctests, helper function requires user input
        """
        amount = self.get_bet()
        while not self.valid_bet(amount):
            print(f"That is an invalid bet. Please input an amount within ${MINIMUM_BET()} and ${self.balance}\n")
            amount = self.get_bet()
        self.balance -= amount
        self.bet = amount
        print(f"A total of ${self.bet} has been deducted from your balance. Good luck, player!\n")
        time.sleep(1)

    def collect(self, bonus=1):
        """Collect the bet amount multiplied by a bonus.

        Default value of bonus is 1, meaning no bonus.

        :param bonus: an integer
        :precondition: bonus is the bonus multiplier for the collected bet when a player has won
        :postcondition: the Bank.balance appropriately increments by the bank.bet amount multiplied by the bonus
        :return: None, the Bank.balance is modified

        Unable to test with actual bet > 0 due to requirement of user input

        >>> my_bank = Bank()
        >>> my_bank.collect(1)
        A total of $0 has been collected to your balance.
        <BLANKLINE>
        >>> my_bank.balance
        100
        """
        collect_amount = self.bet * bonus
        self.balance += collect_amount
        print(f"A total of ${collect_amount} has been collected to your balance.\n")

    def report_balance(self):
        """Print the current balance in the bank.

        :postcondition: the current balance is printed to the user
        :return: None, the current balance reported to the user

        >>> my_bank = Bank()
        >>> my_bank.report_balance()
        The current balance in your account is $100.
        <BLANKLINE>
        """
        print(f"The current balance in your account is ${self.balance}.\n")


class Report:

    def __init__(self):
        """Instantiate a Report class.

        :postcondition: an object of the Report class is instantiated with attributes wins, losses, and draws
        :postcondition: wins is an integer that will store the number of wins by the main player
        :postcondition: losses is an integer that will store the number of losses by the main player
        :postcondition: draws is an integer that will store the number of draws by the main player
        :return: an instance of the Report class

        >>> game_report = Report()
        >>> game_report.wins
        0
        >>> game_report.losses
        0
        >>> game_report.draws
        0
        """
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def __str__(self):
        """Return the string when this report is printed.

        :return: a string, the returned string if the report is passed to print

        >>> game_report = Report()
        >>> print(game_report)
        WINS: 0, LOSSES: 0, DRAWS: 0
        """
        return f"WINS: {self.wins}, LOSSES: {self.losses}, DRAWS: {self.draws}"

    def __repr__(self):
        """Return the official string representation of the report.

        :return: a string, the official string representation of this report

        >>> game_report = Report()
        >>> game_report
        Report(0, 0, 0)
        """
        return f"Report({self.wins}, {self.losses}, {self.draws})"

    def record(self, result: str):
        """Record a loss, win, or top_draw in the report object.

        :param result: a string
        :precondition: result is a string of either "draw", "win" or "lose"
        :postcondition: increments record.loss by 1 if result == "lose"
        :postcondition: increments record.win by 1 if result == "win"
        :postcondition: increments record.draw by 1 if result == "draw"
        :return: None, modifies either record.loss, record.win, or record.draw appropriately

        >>> game_report = Report()
        >>> game_report.record(result="win")
        >>> game_report
        Report(1, 0, 0)
        >>> game_report.record("lose")
        >>> game_report
        Report(1, 1, 0)
        >>> game_report.record("draw")
        >>> game_report
        Report(1, 1, 1)
        """
        if result == "win":
            self.wins += 1
        elif result == "lose":
            self.losses += 1
        elif result == "draw":
            self.draws += 1

    def report_rounds(self):
        """Print the total rounds played.

        :postcondition: accurately sum up wins, losses, and draws to produce the total number of rounds
        :return: an integer, the sum of all rounds that have been played

        >>> game_report = Report()
        >>> game_report.report_rounds()
        Total Rounds played: 0
        >>> game_report.record(result="win")
        >>> game_report
        Report(1, 0, 0)
        >>> game_report.record("lose")
        >>> game_report
        Report(1, 1, 0)
        >>> game_report.record("draw")
        >>> game_report
        Report(1, 1, 1)
        >>> game_report.report_rounds()
        Total Rounds played: 3
        """
        return print(f"Total Rounds played: {sum([self.wins, self.draws, self.losses])}")


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

    >>> my_person = Player()
    >>> my_deck = CardDeck()
    >>> draw_card(my_person, my_deck)
    <BLANKLINE>
    -----> User draws 2 of Diamonds with a value of 2
    Their current total hand is 2.
    >>> my_person.total
    2
    >>> my_person.hand
    [Card(2, 2, Diamonds)]
    """
    drawing_player = "Dealer" if person.dealer else "User"
    for _ in range(times):
        try:
            card = deck.top_draw()
        except IndexError:
            print("We've reached the bottom of the deck!")
        else:
            if card.face == "Ace":
                person.aceCount += 1
            person.hand.append(card)
            person.total += card.value
            print(f"\n-----> {drawing_player} draws {card.__str__()}\n"
                  f"Their current total hand is {person.total}.")
            time.sleep(1)


def bust(person):
    """Determine if the person has busted.

    Bust meaning the total points in their hand has hit > BUST_LIMIT()

    :param person: a Player
    :precondition: person is an instance of the Player class
    :postcondition: return True of False if the person has busted
    :postcondition: a player is bust if their total points is > BUST_LIMIT()
    :return: Boolean, True/False if player's total is > BUST_LIMIT()

    >>> my_player = Player()
    >>> my_player.total = 0
    >>> bust(my_player)
    False
    >>> my_player.total = GOAL_TOTAL() // 2
    >>> bust(my_player)
    False
    >>> my_player.total = GOAL_TOTAL()
    >>> bust(my_player)
    False
    >>> my_player.total = GOAL_TOTAL() + 1
    >>> bust(my_player)
    True
    """
    if person.total > GOAL_TOTAL() and person.aceCount == 0:
        return True
    elif person.total > GOAL_TOTAL() and person.aceCount > 0:
        adjust_ace(person)
        return person.total > GOAL_TOTAL()
    else:   # person.total <= GOAL_TOTAL()
        return False


def adjust_ace(person):
    """Adjust the person's total score if they have an ace on hand.

    :param person: a Player
    :precondition: person is an instance of the Player class
    :postcondition: the player's total score is adjusted if and only if they have an ace on hand and their current
                    total score exceeds that the BUST_LIMIT()
    :postcondition: should the player meet any of the two conditions for adjustment, the person's score is subtracted
                    by 10 for each ace they have on hand until their total is <= BUST_LIMIT()
    :return: None, the player's total score possibly modified

    >>> my_player = Player()
    >>> my_player.total = GOAL_TOTAL() + 1
    >>> my_player.aceCount = 2
    >>> adjust_ace(my_player)
    <BLANKLINE>
    An Ace value in this player's hand has been adjusted to 1 for a new total of 12
    >>> my_player.total = GOAL_TOTAL()
    >>> my_player.aceCount = 2
    >>> adjust_ace(my_player)

    >>> my_player.total = GOAL_TOTAL() - 1
    >>> my_player.aceCount = 1
    >>> adjust_ace(my_player)

    >>> my_player.total = GOAL_TOTAL() + 11
    >>> my_player.aceCount = 2
    >>> adjust_ace(my_player)
    <BLANKLINE>
    An Ace value in this player's hand has been adjusted to 1 for a new total of 22
    <BLANKLINE>
    An Ace value in this player's hand has been adjusted to 1 for a new total of 12
    """
    while person.total > GOAL_TOTAL() and person.aceCount != 0:
        person.total -= ACE_MODIFIER()
        person.aceCount -= 1
        print(f"\nAn Ace value in this player's hand has been adjusted to "
              f"1 for a new total of {person.total}")


def number_print(items: iter) -> None:
    """Print menu options for a given tuple of menu options.

    :param items: an iterable data type
    :precondition: items is an iterable data-type containing elements
    :postcondition: print enumerated items starting from 1
    :return: prints enumerated options as strings starting from 1

    >>> no_items = []
    >>> number_print(no_items)

    >>> items_tuple = ('apples', 'oranges', 'peaches')
    >>> number_print(items_tuple)
    [1] apples
    [2] oranges
    [3] peaches
    >>> items_list = ['muffins', 'croissants', 'cake']
    >>> number_print(items_list)
    [1] muffins
    [2] croissants
    [3] cake
    """
    for number, option in enumerate(items, 1):
        print(f"[{number}] {option}")


# -----------------START GAME-------------------------------------------------------------------------------------------


def start_game() -> tuple:
    """Start the game by producing the necessary components for the game.

    :postcondition: returns the necessary components: user's player, dealer, bank, deck, and report for the game
                    as a tuple
    :return: a tuple of the necessary game components

    No doctests, deck.shuffle uses random module
    """
    print(WELCOME())
    score_report, bank = Report(), Bank()
    deck = CardDeck()
    deck.shuffle()
    return score_report, bank, deck


# -----------------END GAME---------------------------------------------------------------------------------------------

def end_game(bank, card_deck) -> bool:
    """Determine if the game should end.

    Game will end if deck of cards in game has been exhausted or if the player's bank balance is < MINIMUM_BET()

    :postcondition: return True if the game must end (i.e. deck of cards is empty or player's bank balance is <
                    MINIMUM_BET()
    :postcondition: return False if game does not meet end-game requirements and must continue
    :return: Boolean

    >>> piggy_bank = Bank()
    >>> my_deck = CardDeck()
    >>> end_game(piggy_bank, my_deck)
    False
    >>> piggy_bank.balance = MINIMUM_BET()
    >>> end_game(piggy_bank, my_deck)
    False
    >>> piggy_bank.balance = MINIMUM_BET() - 1
    >>> end_game(piggy_bank, my_deck)
    You're broke and you've run out of money! :(
    <BLANKLINE>
    True
    >>> piggy_bank.balance = START_BANK()
    >>> my_deck.cards = []
    >>> end_game(piggy_bank, my_deck)
    We've exhausted the deck of cards.
    <BLANKLINE>
    True
    """
    if bank.balance < MINIMUM_BET():
        print("You're broke and you've run out of money! :(\n")
    elif not card_deck.cards:
        print("We've exhausted the deck of cards.\n")
    return bank.balance < MINIMUM_BET() or not card_deck.cards

# -----------------PLAY ROUND-------------------------------------------------------------------------------------------


def start_round(user, dealer, deck):
    """Begin the round by having player and dealer draw 2 cards each.

    :param user: a Player
    :param dealer: a Player
    :param deck: a CardDeck
    :precondition: the user and dealer are instances of the Player class
    :precondition: the deck is an instance of the CardDeck class
    :postcondition: the user and dealer receives 2 cards to their hand by drawing from the deck
    :postcondition: the deck will have cards reduced in its deck.cards attribute by at most, 4 cards
    :return: None, user, dealer, and deck attributes likely modified

    >>> my_deck = CardDeck()
    >>> bob = Player()
    >>> my_dealer = Player(dealer=True)
    >>> start_round(bob, my_dealer, my_deck)
    <BLANKLINE>
    ======== INITIAL DEAL ========
    <BLANKLINE>
    -----> Dealer draws 2 of Diamonds with a value of 2
    Their current total hand is 2.
    <BLANKLINE>
    -----> Dealer draws 2 of Hearts with a value of 2
    Their current total hand is 4.
    <BLANKLINE>
    -----> User draws 2 of Clubs with a value of 2
    Their current total hand is 2.
    <BLANKLINE>
    -----> User draws 2 of Spades with a value of 2
    Their current total hand is 4.
    <BLANKLINE>
    This concludes the initial deal:
    \033[36mPlayer: 4\033[0m
    \033[33mDealer: 4\033[0m
    <BLANKLINE>
    >>> my_dealer.hand
    [Card(2, 2, Diamonds), Card(2, 2, Hearts)]
    >>> my_dealer.total
    4
    >>> bob.hand
    [Card(2, 2, Clubs), Card(2, 2, Spades)]
    >>> bob.total
    4
    """
    print("\n======== INITIAL DEAL ========")
    draw_card(dealer, deck, 2)
    draw_card(user, deck, 2)
    print(f"\nThis concludes the initial deal:\n"
          f"\033[36mPlayer: {user.total}\033[0m\n"
          f"\033[33mDealer: {dealer.total}\033[0m\n")
    time.sleep(1.5)


def dealer_turn(dealer, deck):
    """Execute the dealer's turn to draw until they hit their STAND_LIMIT(), the deck is exhausted, or they bust.

    :param dealer: a Player
    :param deck: a CardDeck
    :precondition: the dealer is an instance of a Player class
    :precondition: a deck is an instance of a CardDeck class
    :postcondition: the dealer will draw until the card deck is exhausted, they have reached STAND_LIMIT(), or
                    they bust
    :return: None, the dealer's hand and the deck may be modified

    >>> my_dealer = Player(dealer=True)
    >>> my_deck = CardDeck()
    >>> my_dealer.total = 14
    >>> dealer_turn(my_dealer, my_deck)
    <BLANKLINE>
    ======== DEALER'S TURN ========
    <BLANKLINE>
    -----> Dealer draws 2 of Diamonds with a value of 2
    Their current total hand is 16.
    <BLANKLINE>
    The dealer Stands, their total is \033[33m16\033[0m.
    <BLANKLINE>
    >>> my_dealer.total = STAND_LIMIT()
    >>> dealer_turn(my_dealer, my_deck)
    <BLANKLINE>
    ======== DEALER'S TURN ========
    <BLANKLINE>
    The dealer Stands, their total is \033[33m15\033[0m.
    <BLANKLINE>
    >>> my_dealer.total = GOAL_TOTAL() + 1
    >>> dealer_turn(my_dealer, my_deck)
    <BLANKLINE>
    ======== DEALER'S TURN ========
    <BLANKLINE>
    The dealer Stands, their total is \033[33m22\033[0m.
    <BLANKLINE>
    >>> my_dealer.total = 10
    >>> my_deck.cards = []
    >>> dealer_turn(my_dealer, my_deck)
    <BLANKLINE>
    ======== DEALER'S TURN ========
    <BLANKLINE>
    The dealer Stands, their total is \033[33m10\033[0m.
    <BLANKLINE>
    """
    print("\n======== DEALER'S TURN ========")
    while deck.cards and not bust(dealer) and dealer.total < STAND_LIMIT():
        draw_card(dealer, deck)
    print(f"\nThe dealer Stands, their total is \033[33m{dealer.total}\033[0m.\n")
    time.sleep(1)


def player_turn(user, deck):
    """Execute the player's turn to draw until player decides to stand, the deck is exhausted, or they bust.

    :param user: a Player
    :param deck: a CardDeck
    :precondition: the user is an instance of a Player class
    :precondition: a deck is an instance of a CardDeck class
    :postcondition: the user will be asked if they would like to draw until the card deck is exhausted, they bust,
                    or user decides to stand
    :return: None, user and deck attributes possibly modified

    No doctests, player input required
    """
    print(f"\n======== PLAYER'S TURN ========\n\n"
          f"Your current hand is \033[36m{user.total}\033[0m.\n")
    while deck.cards and not bust(user):
        if player_draw():
            draw_card(user, deck)
        else:
            print(f"\nYou've chosen to Stand, this ends the round with your hand of \033[36m{user.total}\033[0m.\n")
            break
    time.sleep(1)


def player_draw():
    """Return if the player wants to draw another card.

    :postcondition: return Boolean True if player wants to draw another card, return Boolean False if player
                    does not want to draw another card
    :return: Boolean

    No doctests, player input required
    """
    print("\nWhat would you like to do?\n")
    number_print(TURN_OPTIONS())
    user_decision = input("Enter the number of your decision: ")
    return user_decision == "1"


def play_round(user, dealer, deck):
    """Execute a full round of BlackJack between a player and dealer.

    :param user: a Player
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
    start_round(user=user, dealer=dealer, deck=deck)
    dealer_turn(dealer, deck)
    if dealer.total <= GOAL_TOTAL():
        player_turn(user, deck)


# -----------------ENDING THE ROUND-------------------------------------------------------------------------------------

def decide_winner(user, dealer):
    """Determine who the winner is based on the total results.

    :param user: a Player
    :param dealer: a Player
    :precondition: the user and dealer are instances of the Player class
    :postcondition: return a draw if both user and dealer's total scores are equal
    :postcondition: return 'user' if the dealer's hand is bust or if user's total is > dealer's total
    :postcondition: return 'dealer' if the user's hand is bust or if dealer's total is > player's total
    :return: a string, either 'draw', 'user' or 'dealer'

    >>> my_player = Player()
    >>> my_dealer = Player(dealer=True)

    >>> my_dealer.total = GOAL_TOTAL() + 1
    >>> decide_winner(my_player, my_dealer)
    <BLANKLINE>
    This round, your total hand is 0 and the dealer's total hand is 22
    'user'
    >>> my_dealer.total = GOAL_TOTAL() - 1
    >>> my_player.total = GOAL_TOTAL() + 1
    >>> decide_winner(my_player, my_dealer)
    <BLANKLINE>
    This round, your total hand is 22 and the dealer's total hand is 20
    'dealer'
    >>> my_dealer.total = 10
    >>> my_player.total = 19
    >>> decide_winner(my_player, my_dealer)
    <BLANKLINE>
    This round, your total hand is 19 and the dealer's total hand is 10
    'user'
    >>> my_dealer.total = 20
    >>> my_player.total = 18
    >>> decide_winner(my_player, my_dealer)
    <BLANKLINE>
    This round, your total hand is 18 and the dealer's total hand is 20
    'dealer'
    >>> my_dealer.total = 5
    >>> my_player.total = 5
    >>> decide_winner(my_player, my_dealer)
    <BLANKLINE>
    This round, your total hand is 5 and the dealer's total hand is 5
    'draw'
    """
    print(f"\nThis round, your total hand is {user.total} and the dealer's total hand is {dealer.total}")
    if bust(dealer):
        return "user"
    if bust(user):
        return "dealer"
    if user.total > dealer.total:
        return "user"
    if user.total < dealer.total:
        return "dealer"
    else:   # tie
        return "draw"


def win_round(bank, report):
    """Make win round modifications to bank and report.

    :param bank: a Bank
    :param report: a Report
    :precondition: bank is an instance of the Bank class
    :precondition: report is an instance of the Report class
    :postcondition: the bank collects winnings from the bet with a WIN_BONUS() multiplier
    :postcondition: the report updates and increments the report.wins by 1
    :return: None, report and bank attributes updated

    >>> my_bank = Bank()
    >>> my_report = Report()
    >>> my_bank.balance = 190
    >>> my_bank.bet = 10
    >>> win_round(my_bank, my_report)
    <BLANKLINE>
    YOU WIN THIS ROUND!!!
    You get to collect 2x the bet you placed!
    Hope you can use this towards your student loans ;)
    <BLANKLINE>
    A total of $20 has been collected to your balance.
    <BLANKLINE>
    >>> my_bank.balance
    210
    >>> my_report
    Report(1, 0, 0)
    """
    print(f"\nYOU WIN THIS ROUND!!!\n"
          f"You get to collect {WIN_BONUS()}x the bet you placed!\n"
          f"Hope you can use this towards your student loans ;)\n")
    bank.collect(WIN_BONUS())
    report.record(result="win")


def lose_round(report):
    """Make loss round modifications to bank and report.

    :param report: a Report
    :precondition: bank is an instance of the Bank class
    :precondition: report is an instance of the Report class
    :postcondition: the report updates and increments the report.losses by 1
    :return: None, report.loss attribute updated

    >>> my_report = Report()
    >>> lose_round(my_report)
    You've lost this round, sorry my friend :(
    <BLANKLINE>
    >>> my_report
    Report(0, 1, 0)
    >>> lose_round(my_report)
    You've lost this round, sorry my friend :(
    <BLANKLINE>
    >>> my_report
    Report(0, 2, 0)
    """
    print("You've lost this round, sorry my friend :(\n")
    report.record(result="lose")


def draw_round(bank, report):
    """Make draw round modifications to bank and report.

    :param bank: a Bank
    :param report: a Report
    :precondition: bank is an instance of the Bank class
    :precondition: report is an instance of the Report class
    :postcondition: the bank collects back the bet amount
    :postcondition: the report updates and increments the report.draws by 1
    :return: None, report and bank attributes updated

    >>> my_bank = Bank()
    >>> my_report = Report()
    >>> my_bank.balance = 50
    >>> my_bank.bet = 15
    >>> draw_round(my_bank, my_report)
    Bizarre! Looks like it was a tie. You get your money back. :)
    <BLANKLINE>
    A total of $15 has been collected to your balance.
    <BLANKLINE>
    >>> my_bank.balance
    65
    >>> my_report
    Report(0, 0, 1)
    """
    print("Bizarre! Looks like it was a tie. You get your money back. :)\n")
    bank.collect()
    report.record(result="draw")


def end_round(winner_result, bank, report):
    """End the round appropriately based on the results of the win for a round.

    :param winner_result: a string
    :param bank: a Bank
    :param report: a Report
    :precondition: winner_result is a string of either "draw", "user", or "dealer"
    :precondition: bank is an instance of the Bank class
    :precondition: report is an instance of the Report class
    :postcondition: the bank and report is appropriately modified based on winner_results by being passed to
                    the correct helper functions for winning, losing, or draws
    :return: None, the bank and report modified based on the winner_result

    >>> my_bank = Bank()
    >>> my_bank.bet = 10
    >>> my_report = Report()

    >>> end_round("draw", my_bank, my_report)
    Bizarre! Looks like it was a tie. You get your money back. :)
    <BLANKLINE>
    A total of $10 has been collected to your balance.
    <BLANKLINE>
    >>> my_bank.balance
    110
    >>> my_report
    Report(0, 0, 1)

    >>> end_round("user", my_bank, my_report)
    <BLANKLINE>
    YOU WIN THIS ROUND!!!
    You get to collect 2x the bet you placed!
    Hope you can use this towards your student loans ;)
    <BLANKLINE>
    A total of $20 has been collected to your balance.
    <BLANKLINE>
    >>> my_bank.balance
    130
    >>> my_report
    Report(1, 0, 1)

    >>> end_round("dealer", my_bank, my_report)
    You've lost this round, sorry my friend :(
    <BLANKLINE>
    >>> my_bank.balance
    130
    >>> my_report
    Report(1, 1, 1)
    """
    if winner_result == "draw":
        draw_round(bank, report)
    elif winner_result == "user":
        win_round(bank, report)
    else:   # winner_result == "dealer"
        lose_round(report)


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

    No doctests, player input required
    """
    score_report, bank, game_deck = start_game()
    while not end_game(bank, game_deck):
        user, dealer = Player(), Player(dealer=True)
        bank.report_balance()
        bank.place_bet()
        play_round(user=user, dealer=dealer, deck=game_deck)
        if game_deck.cards:
            winner = decide_winner(user, dealer)
            end_round(winner_result=winner, bank=bank, report=score_report)
    print(score_report)
    score_report.report_rounds()
    print("This concludes our game of BlackJack 21, thank you for playing!")


if __name__ == '__main__':
    blackjack()
