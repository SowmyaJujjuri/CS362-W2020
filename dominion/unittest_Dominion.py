from unittest import TestCase
import testUtility
import Dominion

class TestAction_card(TestCase):
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

        coins = 1
        buys = 0
        actions = 0
        cards = "action"
        cost = 0
        name = "Woodcutter"

        actionCard = Dominion.Action_card(self.name, cost, actions, cards, buys, coins)

        self.assertEqual(name, actionCard.name)
        self.assertEqual(actions, actionCard.actions)
        self.assertEqual(cards, actionCard.cards)
        self.assertEqual(buys, actionCard.buys)
        self.assertEqual(coins, actionCard.coins)
    def test_use(self):
        player = "Annie"

        player.played.append(self)
        player.hand.remove(self)
