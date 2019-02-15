class Player:

    """ A class representing a player (in a game) """

    def __init__(self, gold_coins=0, health_points=10, lives=5):
        self.gold_coins = gold_coins
        self.health_points = health_points
        self.lives = lives

    def __str__(self):
        return "Player (>'-')>\nlives: {}\thealth_points: {}\tgold_coins: {}".format(self.lives, self.health_points, self.gold_coins)

# test 1 - printing the object
p1 = Player()
print(p1)
