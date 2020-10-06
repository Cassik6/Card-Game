# Card game

![card game](https://media.giphy.com/media/l2SpSTFjV2I3Hmpgs/giphy.gif)

## Description
You will need to create a card game in python.

## Instructions

### Cards
Create a `Card` class containing:
- A `color`  -> `string`
- A `number` -> `int`
- A `symbol` -> `string`
Symbols are: `[♥, ♦, ♣, ♠]`

### Board
Create a `Board` class containing:
- A list of `Player` nammed `players`
- a list of active `Card` (the 6 last played card are active) nammed `active_cards`
- a list of played `Card` (should not contain the 6 last cards, those should be in the active list) nammed `played_cards`

### Player
Create a class Player containing:
- A name nammed `name`
- A list of `Card` (each player start with 10 Card) nammed `cards`
- A `play()` method that throw a `Card` in the `Board`
- A `shuffle()` method that shuffle all the `Card` of the player.

You have a deck of 52 Cards, containing [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K] for each symbol. All those cards has to be shuffled and distributted between all the players.


### Run the game!
Create a loop so each player `play()` turn by turn until they don't have any `Card` left.
At the end of each turn, print the played card history and the active cards.

## File structure
- All the class declaration should be in a `game.py` file which should be in a `utils` folder. 
- All the code that run the game (the main loop) should be in a main.py file.  
This loop should be in the `main.py` file.


## Constraints
- Add **typing** and **docstrings** for **each functions and classes**.
- Typing should be complete. If you use a list of string, you should specify it in your typing. Same for complexe dict typing. See typing module for more informations.
- Clean the code before sending it to code review.
- Comment your code in a way that make sense.
