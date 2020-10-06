# Card game

![card game](https://media.giphy.com/media/l2SpSTFjV2I3Hmpgs/giphy.gif)

# Objective

Make a card game that actually works!

# Motivations

Because people need to play!

# Contributor

Mysellf AKA Opap's Ditudidi

# Context

-Individual challenge
-Deadline : yesterday
-Duration : 1 day
-Purpose of the Challenge : evaluate Python skills

# What does it do?

-Creates a deck of 52 distinct traditonnal cards and shuffles them.
-Creates 5 players and adds them to the Board.
-Deals the 52 cards as equally as possible to the 5 players
-As long as at least one player has a card, a new round will be started
-Each round, each player who can will play a card.
-Prints the round, the players's plays and the amount oof cards left in each player's deck.
-When there are no more cards left to play. The game ends

# Objects

## Card
field name|type|description
---|---|---
color|str|color of the (will be derived from the symbol)
number|Union[str, int]|number/figure of the cards
symbol|str|symbol of the card
 
## Board
field name|type|description
---|---|---
players|List[Player]|list of all the players playing on the board
active_cards|List[Card]|list of the last 6 (or less) played cards. 
active_cards|List[Card]|list of all the played cards, except for the active cards.

## Player
field name|type|description
---|---|---
name|str|name of the player
cards|List[Card]|list of the cards owned by the player. 

# Development

First I started by making the 3 classes in the game file.
Since they had to reference each other, I had to do research about references classes from the same file.
Afterwards I started workig on the main file. After fixing a few bugs it was functionnal.


# Lessons learned:/encountered difficulties
-How to work with multiple Python files
-How to reference different class objects from the same file
-Make a proper ´docstring´
-Use of ´Union´ for type declaration

# Last minute changes

I realized at the last minute that each player should start with 10 cards, which would make my code so much easier to write.
Since I developped some interesting ways to bypass that I've decided to keep the code as is.

