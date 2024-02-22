class Player:
    def __init__(self, type_):
        self.game = None
        self.num = None
        self.type = type_
        self.money_dict = self.init_money_dict()
        self.money = sum(list(self.money_dict.values()))
        self.position = 0
        self.turns_in_jail = 0
        self.propierties = {}

    def set_data(self, game, num):
        self.game = game
        self.num = num

    def __eq__(self, other):
        return self.num == other.num

    def move(self, dices):
        self.turns_in_jail -= 1
        if self.turns_in_jail > 0:
            ### TODO: check if the player get two equal dices and can scape of jail
            return

        self.position = (self.position + dices) % 40
        self.game.fall_in(self.position)

        # What the player do...

    # TODO: Update the money_dict
    def pay(self, amount):
        self.money -= amount

    def go_to_jail(self):
        self.turns_in_jail = 3
        self.position = 10

    def init_money_dict(self):
        return {1: 10, 5: 5, 10: 5, 20: 5, 50: 5, 100: 2, 500: 2}
