"Main Python file for the card game, this is where the game is launched "

import random as rd
from typing import List

from utils import game


# Creating the deck
cards = []
for i in ["♥", "♦", "♣", "♠"]:
    for j in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:
        cards.append(game.Card(j, i))

# Shuffling the cards
rd.shuffle(cards)

# Creating players
players = (
    game.Player("Jean"),
    game.Player("Remi"),
    game.Player("Dora"),
    game.Player("Sisi"),
    game.Player("Popol"),
)

# Creating the board
board = game.Board(players)

# Dealing the 52 cards
i = 0
while i < len(cards):
    for player in board.players:
        player.cards.append(cards[i])
        i += 1
        if i > len(cards) - 1:
            break


# if there are still cards in any deck, play a round
i = 1
while board.count_cards_left() > 0:
    announcement = f"This is Round {i}: \n"
    i += 1

    # foreach player that has cards, play one and add it to the announcement
    for player in board.players:
        if len(player.cards) > 0:
            announcement += player.play(board)

    print(announcement + board.display_active_cards())

print('\n GAME OVER')
