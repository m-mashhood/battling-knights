import unittest

from game import Game


class TestCase(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def testExecuteMove(self):
        self.game.execute_move('R', 'S')

        self.assertEqual(self.game.R.pos.x, 0)
        self.assertEqual(self.game.R.pos.y, 1)

    def testKnightsWithItem(self):
        self.game.execute_move('B', 'N')
        self.game.execute_move('B', 'N')
        self.game.execute_move('B', 'E')
        self.game.execute_move('B', 'E')

        self.assertEqual(self.game.B.pos.x, 2)
        self.assertEqual(self.game.B.pos.y, 5)
        self.assertEqual(self.game.B.item, self.game.M)
        self.assertEqual(self.game.B.get_total_defense_score(), 2)
        self.assertEqual(self.game.B.get_total_attack_score(), 2)

    def testKnightDrown(self):
        self.game.execute_move('Y', 'N')
        self.assertEqual(self.game.Y.status, 'DROWNED')

    def testBattle(self):
        self.game.execute_move('B', 'E')
        self.game.execute_move('B', 'E')
        self.game.execute_move('B', 'N')
        self.game.execute_move('B', 'N')

        self.game.execute_move('R', 'E')
        self.game.execute_move('R', 'E')
        self.game.execute_move('R', 'S')
        self.game.execute_move('R', 'S')
        self.game.execute_move('R', 'S')
        self.game.execute_move('R', 'S')
        self.game.execute_move('R', 'S')

        self.assertEqual(self.game.R.pos.x, 2)
        self.assertEqual(self.game.R.pos.y, 5)
        self.assertEqual(self.game.R.status, 'LIVE')
        self.assertEqual(self.game.B.status, 'DEAD')


if __name__ == '__main__':
    unittest.main()
