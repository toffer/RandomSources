import unittest

import randomSources

class TestQuantumRandom(unittest.TestCase):

    def setUp(self):
        self.rng = randomSources.QuantumRandom()

    def test_quantum_randrange(self):
        self.assertTrue(self.rng.randrange(100) in range(0, 100))

    def test_quantum_randrange_start_stop(self):
        self.assertTrue(self.rng.randrange(10, 100) in range(10, 100))

    def test_quantum_choice(self):
        self.assertTrue(self.rng.choice(['a', 'b', 'c']) in ['a', 'b', 'c'])

    def test_quantum_shuffle(self):
        orig = list('A23456789JQK')
        cards = list('A23456789JQK')
        self.rng.shuffle(cards)
        self.assertEqual(set(cards), set(orig))

    def test_quantum_sample(self):
        cards = list('A23456789JQK')
        self.assertTrue(set(self.rng.sample(cards, 5)).issubset(set(cards)))


class TestRandomDotOrg(unittest.TestCase):

    def setUp(self):
        self.rng = randomSources.RandomDotOrg()

    def test_randomdotorg_randrange(self):
        self.assertTrue(self.rng.randrange(100) in range(100))

    def test_randomdotorg_randrange_start_stop(self):
        self.assertTrue(self.rng.randrange(10, 100) in range(10, 100))

    def test_randomdotorg_choice(self):
        self.assertTrue(self.rng.choice(['a', 'b', 'c']) in ['a', 'b', 'c'])

    def test_randomdotorg_shuffle(self):
        orig = list('A23456789JQK')
        cards = list('A23456789JQK')
        self.rng.shuffle(cards)
        self.assertEqual(set(cards), set(orig))

    def test_randomdotorg_sample(self):
        cards = list('A23456789JQK')
        self.assertTrue(set(self.rng.sample(cards, 5)).issubset(set(cards)))


if __name__ == '__main__':
    unittest.main()
