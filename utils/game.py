"Main classes needed foor the card game"

from random import shuffle
from typing import Union, List, Type
import random as rd


class Card:
    """
    A class used to represent a Card.
    Validation happens during __init__

    Attributes
    ----------
    color : str
        Color of the card
    number : Union[int, str]
        Number or figure of the card
    symbol : str
        Symbol of the card

    Methods
    -------

    display() -> str
        returns a string with the card number and symbol
    """

    def __init__(self, number: Union[int, str], symbol: str):
        # validation
        if type(number) == int and (number > 1 and number < 11):
            self.number = number
        elif type(number) == str and number in ["A", "J", "Q", "K"]:
            self.number = number
        # validation
        if symbol in ["♥", "♦", "♣", "♠"]:
            self.symbol = symbol
            # using the symbol to determine the color
            if symbol in ["♥", "♦"]:
                self.color = "Red"
            else:
                self.color = "Black"

    def dislay(self) -> str:
        return f"{self.number} {self.symbol}"


class Player:
    """
    A class used to represent a Board

    Attributes
    ----------
    name : string
        Name of the player

    cards : list
        List of Card objects (each player start with 10 Card)

    played_cards : list
        Symbol of the card if any
    list of played Card objects (should not contain the 6 last cards, those should be in the active list)

    Methods
    -------
    play(card, board) -> str
        Shuffles all the cards and then throws a card in the board, returns a string of the players name and the card he played
    shuffle()
        Shuffles all the cards of the player
    """

    def __init__(self, name: str):
        self.cards: List[Card] = []
        self.name = name

    def play(self, board: "Board") -> str:
        # if the player still has cards, play it and add it to the active cards f the board
        if len(self.cards) > 0:
            self.shuffle()
            # I dont like modifying the board here, but specifications implies it should be done in this class.
            card_to_play = self.cards[0]
            board.active_cards.append(card_to_play)
            # if the board has already 6 cards, remove the last one and add the new one
            if len(board.active_cards) > 6:
                board.played_cards.append([board.active_cards[0]])
                board.active_cards.remove(board.active_cards[0])
            self.cards.remove(card_to_play)
            return f"{self.name} played {card_to_play.dislay()}\n"
        return f"{self.name} played nothing"

    def shuffle(self):
        if len(self.cards) > 0:
            rd.shuffle(self.cards)


class Board:
    """
    A class used to represent a Board

    Attributes
    ----------
    players : list
        List of Player objects
    active_cards : list
        List of active Card objects (the 6 last played card are active)
    played_cards : list
        Symbol of the card if any
    list of played Card objects (should not contain the 6 last cards, those should be in the active list)

    Methods
    -------
    count_cards_left()-> int
        Returns the total amount of cards left amongst all the players.

    display_active_cards() -> str
        Returns a string of all the active cards
    """

    def __init__(self, players: List[Type[Player]]):
        self.players = players
        self.active_cards: List[Card] = []
        self.played_cards: List[Card] = []

    def count_cards_left(self) -> int:
        cards_left = sum(len(player.cards) for player in self.players)
        print(f"there are {cards_left} cards left\n")
        return cards_left

    def display_active_cards(self) -> str:
        string_cards = ""
        for card in self.active_cards:
            string_cards += f" {card.dislay()}"
        return f"This are the active cards: {string_cards}"
