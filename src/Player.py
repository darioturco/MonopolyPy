class Player:
    def __init__(self, type_):
        self.game = None
        self.num = None
        self.type = type_
        self.money_dict = self.init_money_dict()
        self.money = sum(list(self.money_dict.values()))
        self.position = 0
        self.turns_in_jail = 0
        self.trains = 0
        self.services = 0
        self.last_dices = 0



    def set_data(self, game, num):
        self.game = game
        self.num = num

    def __eq__(self, other):
        return self.num == other.num

    def move(self, dices):
        """ Advance one move of the player
            Return a boolean that indicate if the player moves or don't """
        self.turns_in_jail -= 1
        if self.turns_in_jail > 0:
            if self.game.dices.go_out_of_jail():
                self.turns_in_jail = 0
            else:
                return False

        self.last_dices = dices
        self.position = self.position + dices
        if self.position >= 40:
            self.position = self.position % 40
            self.money += 200

        self.want_buy_houses()
        self.game.fall_in(self.position)
        return True

    def purchase(self, building):
        self.money -= building.price
        self.game.buildings_purchased[self.position] = building

    def pay(self, amount):
        ### TODO: Update the money_dict
        self.money -= amount

    def go_to_jail(self):
        self.turns_in_jail = 3
        self.position = 10

    def want_to_buy(self):
        ### TODO: change and implement
        # This should be delegated to an external module powered by a RL agent or a human
        return True

    def want_buy_houses(self):
        """ The player decides whether them want to buy some houses """
        ### TODO: delegate to the decision module of the player
        return False

    def init_money_dict(self):
        return {1: 10, 5: 5, 10: 5, 20: 5, 50: 5, 100: 2, 500: 2}
