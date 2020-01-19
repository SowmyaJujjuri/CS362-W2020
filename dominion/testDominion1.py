# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19  13:21:45 2020

@author: Sowmya Jujjuri
"""

import Dominion
import random
import testUtility
from collections import defaultdict

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#number of curses and victory cards
if len(player_names)>2:
    nV=12
else:
    nV=8
nC = -10 + 10 * len(player_names)

box = testUtility.getBoxes(nV)

supply_order = testUtility.getSupplyOrder()

supply = testUtility.getSupply(nV, player_names, box, nC)

#initialize the trash
trash = []

players = testUtility.constructPlayer(player_names)

testUtility.playGame(supply, supply_order, players, trash)
            

testUtility.finalScore(players)
