class player:
    def __init__(self) -> None:
        pass

    hand_token = {'white': 0, 'blue':0, 'green':0, 'red':0, 'black':0, 'yellow':0}
    discount = {'white': 0, 'blue':0, 'green':0, 'red':0, 'black':0, 'yellow':0}
    card = []
    reservation = []

class develope_card:
    def __init__(self, white, blue, green, red, black, score, tier, discount):
        self.price = {'white': white, 'blue':blue, 'green':green, 'red':red, 'black':black}
        self.score = score
        self.tier = tier
        self.discount = discount

player1 = player