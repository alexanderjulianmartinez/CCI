from DeckOfCards.card import Card


class Deck(Card):
    def __init__(self):
        self.cards = []
        self.dealtIndex = 0

    def shuffle(self):
        pass

    def set_deck_of_cards(self, cards):
        self.cards = cards

    def remaining_cards(self):
        return len(self.cards)-self.dealtIndex

    def deal_hand(self, num):
        self.dealtIndex += num

    def deal_card(self):
        self.dealtIndex += 1
