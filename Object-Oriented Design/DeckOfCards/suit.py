from enum import Enum


class Suit(Enum):
    Club, Diamond, Heart, Spade = 0, 1, 2, 3

    def get_suit_value(self):
        return self.value

    def get_suit_from_value(self, value):
        return Suit(value)
