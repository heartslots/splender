class player:
    def __init__(self) -> None:
        pass

    hand_token = {'white': 0, 'blue':0, 'green':0, 'red':0, 'black':0, 'yellow':0}
    discount = {'white': 0, 'blue':0, 'green':0, 'red':0, 'black':0, 'yellow':0}
    card = []

class develope_card:
    def __init__(self, white, blue, green, red, black, score, discount):
        self.price = {'white': white, 'blue':blue, 'green':green, 'red':red, 'black':black}
        self.score = score
        self.discount = discount

player1 = player
player1.hand_token['red'] += 2
print(player1.hand_token)

card1 = develope_card(0,3,3,5,3,3,'blue')
print(card1.price, card1.score, card1.discount)