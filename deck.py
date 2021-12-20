import random

class Card( object ):
    def __init__(self, name, value, suit):
        self.value = value
        self.suit = suit
        self.name = name
        self.showing = False
    def __repr__(self):
        if self.showing:
            return str(self.name) + self.suit
        else:
            return "Card"

class StandardDeck (list):
    def __init__(self):
        self.cards = []
        suits = ["h", "s", "d", "c"]
        values = {"2"   : 2,
                  "3" : 3,
                  "4"  : 4,
                  "5"  : 5,
                  "6"   : 6,
                  "7" : 7,
                  "8" : 8,
                  "9"  : 9,
                  "10"   : 10,
                  "J"  : 11,
                  "Q" : 12,
                  "K"  : 13,
                  "A"   : 14
                  }

        for name in values:
            for suit in suits:
                self.cards.append(Card(name, values[name], suit))

    def __repr__(self):
        return "Standard deck of cards: {0} cards remaining".format(len(self.cards))

    def shuffle(self, times=1):
        random.shuffle(self.cards)
        print("Deck shuffled")

    def deal(self):
        return self.cards.pop(0)
