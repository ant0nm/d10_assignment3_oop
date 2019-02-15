class Player:

    """ A class representing a player (in a game) """

    def __init__(self, lives=5, health_points=10, gold_coins=0):
        self.lives = lives
        self.health_points = health_points
        self.gold_coins = gold_coins

    def __str__(self):
        return "Player (>'-')>\nlives: {}\thealth_points: {}\tgold_coins: {}".format(self.lives, self.health_points, self.gold_coins)

    def level_up(self):
        self.lives += 1

    def collect_treasure(self):
        self.gold_coins += 1
        if self.gold_coins != 0 and self.gold_coins % 10 == 0:
            self.level_up()

    def do_battle(self, damage):
        self.health_points -= damage
        if self.health_points < 1:
            self.lives -= 1
            if self.lives <= 0:
                self.restart()
            else:
                self.health_points = 10

    def restart(self):
        self.lives = 5
        self.health_points = 10
        self.gold_coins = 0

# test 1 - printing the object
p1 = Player()
print(p1)

# test 2 - leveling up
p1.level_up()
print()
print(p1)

# test 3 - collecting treasure
# with leveling up - 10 coins collected
for i in range(1, 11):
    p1.collect_treasure()
print()
print(p1)
# without leveling up - 5 coins collected
for i in range(1, 6):
    p1.collect_treasure()
print()
print(p1)

# test 4 - going into battle
print()
print(p1)
# small damage
p1.do_battle(9)
print()
print("Small damage of 9:")
print(p1)
# large damage
p1.do_battle(18)
print()
print("Large damage of 18:")
print(p1)
# large damage - many times
print()
print("Large damage of 15 continues - 5 times:")
for i in range(1,6):
    p1.do_battle(15)
    if i > 1:
        print()
    print(p1)
# testing the reset
print()
print("Testing reset:")
p1.do_battle(25)
print(p1)
