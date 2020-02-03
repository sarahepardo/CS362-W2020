from unittest import TestCase
import testUtility

class TestCard(TestCase):
    def setUp(self):
        # Data setup
        self.players = testUtility.GetPlayers()
        self.nV = testUtility.GetCurses(self.players)
        self.nC = testUtility.GetVictoryCards(self.players)
        self.box = testUtility.GetBoxes(self.nV)
        self.supply_order = testUtility.GetSupplyOrder()

        #Pick n cards from box to be in the supply.
        self.supply = testUtility.GetSupply(self.box, 5, self.players, self.nV, self.nC)
        self.trash = []

    def test_react(self):
        self.fail()


# Action_card Class
#   1. initialization
#   a. initialization variables
#   b. call the function being tested
#   2. 'use' function
#   3. 'argument'function
#   b. assert expectations when function returns

# Player Class
#   a. initialization variables
#   b. call the function being tested
#   1. 'action_balance' function
#   2. 'calcpoints' function
#   3. 'draw' function
#   4. 'cardsummary' function
#   b. assert expectations when function returns


# gameOver function
#   a. initialization variables
#   b. call the function being tested
#   c. assert expectations when function returns
