from unittest import TestCase
import testUtility
import Dominion

class TestAction_card(TestCase):
    def setUp(self):
        self.player_names = ["Annie","*Ben","*Carla"]
        # Data setup
        if len(self.player_names) > 2:
            self.nV = 12
        else:
            self.nV = 8
        self.nC = -10 + 10 * len(self.player_names)

        self.box = testUtility.getBoxes(self.nV)

        supply_order = {0: ['Curse', 'Copper'], 2: ['Estate', 'Cellar', 'Chapel', 'Moat'],
                        3: ['Silver', 'Chancellor', 'Village', 'Woodcutter', 'Workshop'],
                        4: ['Gardens', 'Bureaucrat', 'Feast', 'Militia', 'Moneylender', 'Remodel', 'Smithy', 'Spy',
                            'Thief', 'Throne Room'],
                        5: ['Duchy', 'Market', 'Council Room', 'Festival', 'Laboratory', 'Library', 'Mine', 'Witch'],
                        6: ['Gold', 'Adventurer'], 8: ['Province']}

        self.supply = testUtility.getSupply(self.nV, self.player_names, self.box, self.nC)
        # initialize the trash
        self.trash = []
        self.players = testUtility.constructPlayer(self.player_names)
        # testUtility.playGame(supply, supply_order, players, trash)
        # testUtility.finalScore(players)

    def test_init(self):
        self.setUp()

        self.coins = 1
        self.buys = 0
        self.actions = 0
        self.cards = 0
        self.cost = 0
        self.name = "Woodcutter"

        actionCard = Dominion.Action_card(self.name, self.cost, self.actions, self.cards, self.buys, self.coins)

        self.assertEqual(self.name, actionCard.name)
        self.assertEqual(self.actions, actionCard.actions)
        self.assertEqual(self.cards, actionCard.cards)
        self.assertEqual(self.buys, actionCard.buys)
        self.assertEqual(self.coins, actionCard.coins)

    def test_use(self):
        self.setUp()
        self.player = Dominion.Player("Annie")

        self.coins = 1
        self.buys = 0
        self.actions = 0
        self.cards = 0
        self.cost = 0
        self.name = "Woodcutter"

        actionCard = Dominion.Action_card(self.name, self.cost, self.actions, self.cards, self.buys, self.coins)
        self.player.hand.append(actionCard)

        played = len(self.player.played)
        hand = len(self.player.hand)

        actionCard.use(self.player, self.trash)

        self.assertEqual(played, len(self.player.played)-1)
        self.assertEqual(hand, len(self.player.hand)+1)

    def test_augment(self):
        self.setUp()
        self.player = Dominion.Player("Annie")

        self.coins = 1
        self.buys = 0
        self.actions = 0
        self.cards = 0
        self.cost = 0
        self.name = "Woodcutter"

        actionCard = Dominion.Action_card(self.name, self.cost, self.actions, self.cards, self.buys, self.coins)

        self.player.buys = 0
        self.player.purse = 0
        self.player.actions = 0

        self.player.hand = []

        actionCard.augment(self.player)

        self.assertEqual(actionCard.actions, self.player.actions)
        self.assertEqual(actionCard.coins, self.player.purse)
        self.assertEqual(actionCard.buys, self.player.buys)
        self.assertEqual(len(self.player.hand), self.cards)

    def test_gameOver(self):
        self.setUp()
        self.test_init()

        self.supply["stack"] = []
        self.supply["stack1"] = []
        self.supply["stack2"] = []

        isGameOver = Dominion.gameover(self.supply)

        self.assertEqual(True, isGameOver)

        self.supply["Province"] = []

        isGameOver2 = Dominion.gameover(self.supply)

        self.assertEqual(True, isGameOver2)










