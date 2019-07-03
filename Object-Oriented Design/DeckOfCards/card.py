from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, c, s):
        self.available = True
        self.faceValue = c
        self.suit = s

    @abstractmethod
    def value(self):
        pass

    def suit(self):
        return self.suit()

    def is_available(self):
        return self.available

    def mark_unavailable(self):
        self.available = False

    def mark_available(self):
        self.available = True
