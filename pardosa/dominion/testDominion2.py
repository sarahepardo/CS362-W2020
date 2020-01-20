# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 15:45:42 2019

@author: sarah pardo
@email: pardosa@oregonstate.edu
"""

import Dominion
import random
import testUtility
from collections import defaultdict


# Get player names
player_names = ["Annie", "*Ben", "*Carla"]

# number of curses and victory cards
nV = 12 if len(player_names) > 2 else 8
nC = -10 + 10 * len(player_names)

# Sorts Card types
box = testUtility.GetBoxes(nV)

supply_order = {0: ['Curse', 'Copper'], 2: ['Estate', 'Cellar', 'Chapel', 'Moat'],
                3: ['Silver', 'Chancellor', 'Village', 'Woodcutter', 'Workshop'],
                4: ['Gardens', 'Bureaucrat', 'Feast', 'Militia', 'Moneylender', 'Remodel', 'Smithy', 'Spy', 'Thief',
                    'Throne Room'],
                5: ['Duchy', 'Market', 'Council Room', 'Festival', 'Laboratory', 'Library', 'Mine', 'Witch'],
                6: ['Gold', 'Adventurer'], 8: ['Province']}


# Pick 10 cards from box to be in the supply and supply card types
supply = testUtility.GetSupply(box, player_names, nV, nC)

# initialize the trash
trash = []

# Costruct the Player objects
players = testUtility.PlayerObject(player_names)

# Plays the game =======================================================================================================
turn = 0
while not Dominion.gameover(supply):
    turn += 4 & turn > 24
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []

for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")

print(dcs)