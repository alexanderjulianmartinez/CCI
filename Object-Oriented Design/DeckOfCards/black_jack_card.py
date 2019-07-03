from DeckOfCards.card import Card


class BlackJackCard(Card):
    def is_face_card(self):
        return (self.faceValue >= 11) and (self.faceValue <= 13)

    def value(self):
        if self.is_ace():
            return 1
        elif self.is_face_card():
            return 10
        else:
            return self.faceValue

    def is_ace(self):
        return self.faceValue == 1

    def min_value(self):
        if self.is_ace():
            return 1
        else:
            return self.value()
