from unittest import TestCase
import testUtility
import Dominion


class TestPlayer(TestCase):
    def setUp(self):
        self.player_names = ["Annie", "*Ben", "*Carla"]
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

        self.name = "Annie"

        self.player = Dominion.Player(self.name)

        self.assertEqual(self.name, self.player.name)

    def test_draw(self):
        self.setUp()
        self.test_init()

        self.coins = 1
        self.buys = 0
        self.actions = 0
        self.cards = 0
        self.cost = 0
        self.name = "Woodcutter"

        actionCard = Dominion.Action_card(self.name, self.cost, self.actions, self.cards, self.buys, self.coins)

        self.player.deck = []
        self.player.discard.append(actionCard)
        hand = len(self.player.hand)

        card = self.player.draw()

        self.assertEqual(0, len(self.player.deck))
        self.assertEqual(0, len(self.player.discard))
        self.assertEqual(hand+1, len(self.player.hand))

    def test_action_balance(self):
        self.setUp()
        self.test_init()
        self.assertEqual(0, self.player.action_balance())

    def test_cardsummary(self):
        self.setUp()
        self.test_init()

        self.coins = 1
        self.buys = 0
        self.actions = 0
        self.cards = 0
        self.cost = 0
        self.name = "Woodcutter"

        actionCard = Dominion.Action_card(self.name, self.cost, self.actions, self.cards, self.buys, self.coins)

        self.player.deck = []
        self.player.hand = []


        self.player.hand.append(actionCard)

        summary = self.player.cardsummary()

        self.assertEqual(1, summary["Woodcutter"])
        self.assertEqual(0, summary["VICTORY POINTS"])

    def test_calcpoints(self):
        self.setUp()
        self.test_init()

        self.assertEqual(3, self.player.calcpoints())
