from unittest import TestCase
import testUtility
import Dominion
import random

class TestPlayer(TestCase):
    def setUp(self):
        player_names = ["Annie"]
        # Data setup
        if len(player_names) > 2:
            nV = 12
        else:
            nV = 8
        nC = -10 + 10 * len(player_names)

        box = testUtility.getBoxes(nV)

        supply_order = {0: ['Curse', 'Copper'], 2: ['Estate', 'Cellar', 'Chapel', 'Moat'],
                        3: ['Silver', 'Chancellor', 'Village', 'Woodcutter', 'Workshop'],
                        4: ['Gardens', 'Bureaucrat', 'Feast', 'Militia', 'Moneylender', 'Remodel', 'Smithy', 'Spy',
                            'Thief', 'Throne Room'],
                        5: ['Duchy', 'Market', 'Council Room', 'Festival', 'Laboratory', 'Library', 'Mine', 'Witch'],
                        6: ['Gold', 'Adventurer'], 8: ['Province']}

        supply = testUtility.getSupply(nV, player_names, box, nC)
        # initialize the trash
        trash = []
        players = testUtility.constructPlayer(player_names)
        testUtility.playGame(supply, supply_order, players, trash)
        testUtility.finalScore(players)

    def test_init(self):
        self.setUp()

        name = "Annie"

        player = Dominion.Player(self.name)


        self.assertEqual(name, player.name)

    def test_cardsummary(self):
        summary = {}
        for c in self.stack():
            if c.name in summary:
                summary[c.name] += 1
            else:
                summary[c.name] = 1
        summary['VICTORY POINTS'] = self.calcpoints()
        return summary
