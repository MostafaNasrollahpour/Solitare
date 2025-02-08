import random


class Cards:
    def __init__(self):
        self.cards = []
        self.init_cards()
        self.shuffle_cards()
        self.get_card()

    def init_cards(self):
        for i in range(13):
            self.cards.append('images/cards/spades_'+str((i + 1)))
            self.cards.append('images/cards/hearts_'+str((i + 1)))
            self.cards.append('images/cards/clubs_'+str((i + 1)))
            self.cards.append('images/cards/diamonds_'+str((i + 1)))

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def get_card(self):
        index = random.randrange(len(self.cards))
        self.cards[index], self.cards[-1] = self.cards[-1], self.cards[index]
        element = self.cards.pop()
        return element
