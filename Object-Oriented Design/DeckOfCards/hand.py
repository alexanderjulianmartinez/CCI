from DeckOfCards.card import Card


class Hand(Card):
    def __init__(self):
        self.cards = []

    def value(self):
        return self.score()

    def score(self):
        score = 0

        for card in self.cards:
            score += card.value()

        return score

    def add_card(self, card):
        self.cards.append(card)
