from unittest import TestCase
from DeckOfCards.suit import Suit


class SuitTests(TestCase):
    def test_init(self):
        suit = Suit(3)
        self.assertEqual(suit.get_suit_value(), 3)

    def test_get_value(self):
        suit = Suit(0)
        self.assertEqual(suit.get_suit_value(), 0)

    def test_get_suit_from_value(self):
        suit = Suit(1)
        self.assertEqual(suit.get_suit_from_value(1), Suit.Diamond)

