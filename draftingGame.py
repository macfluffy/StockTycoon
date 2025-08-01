'''
use numpy module for calculations and randomness
use pytest for testing the code
use rich for prettier text (or use pygame for gui)
more itter tools ?

Class Game
A collection of players each with their own points.

A game consists of 8 players (7 AI). After each player has made 15 picks out of 3 packs, the total value of their portfolio/hand is added up. 
Packs are passed to the right in the first and last rounds. Second round packs are passed to the left. Bonus rewards are given out to players who collect sets.

Class Player
A player will have a hand or collection of stocks/cards, a seat number, a name

Class Hand/Portfolio
A hand consists of a collection of stocks/cards. We add cards/stock to this from packs.

Inside the hand class we calculation the value, based on set collections

Class Stock/Card
Each stock/card has a rarity, name, brand/type and a value.

Class Packs/OpenBids
A pack/open bids is similar to a hand. it consists of a collection of stocks or cards. However these are available to each player to pick one from. Using a round robin system, each person drafts 1 card/stock.

functions:
 initialise()
 Ask for the players name?
 They will be given a seat number

'''

import classes
import botNames
import stockCatalogue

def getDefaultPlayerCount():
    defaultNumberOfPlayers = 8
    return defaultNumberOfPlayers

def gameIsOver(gameOver):
    return True if gameOver else False

if __name__ == '__main__':
    gameOver = False
    
    # Initialise the Game
    newGame = classes.Game(getDefaultPlayerCount())

    # Create the lobby
    nameGenerator = botNames.PlayerNames()
    randomNames = nameGenerator.getAllNames()
    newGame.createPlayers(randomNames)
    newGame.displayGameLobby()

    # Generate the first pack
    stockGenerator = stockCatalogue.StockOptions()
    stockOptions = stockGenerator.getFullCatalogue()
    stockRarities = stockGenerator.getAllRarities()
    newPack = newGame.generatePacks(stockOptions, stockRarities)

    newGame.viewMyPack()
    newGame.askUserToPickStock()
    newGame.displayPlayerPortfolio()
    newGame.passPacks()

    '''while not gameIsOver():'''
    
