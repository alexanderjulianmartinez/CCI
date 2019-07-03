import sys
from DeckOfCards.hand import Hand


class BlackJackHand(Hand):
    def score(self):
        scores = self.possible_scores()
        max_under = -sys.maxsize - 1
        min_over = sys.maxsize

        for score in scores:
            if (score > 21) and (score < min_over):
                min_over = score
            elif (score <= 21) and (score > max_under):
                max_under = score

        return min_over if max_under == -sys.maxsize-1 else max_under

    def possible_scores(self):
        scores = []
        return scores

    def busted(self):
        return self.score() > 21

    def is_21(self):
        return self.score() == 21

    def is_black_jack(self):
        ...
