class Player:


    def __init__(self, type_, game, num):
        self.game = game
        self.num = num
        self.type = type_
        self.money = self.init_money_dict()
        self.position = 0
        self.turns_in_jail = 0

    def move(self, dices):
        self.position = (self.position + dices) % 40

        # Chack if the player whant to buy houses or don't

        self.game.fall_in(self.position)

        # What the player do...

    def init_money_dict(self):
        return {1: 10, 5: 5, 10: 5, 20: 5, 50: 5, 100: 2, 500: 2}
