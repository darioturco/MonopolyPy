from src.agents.interactiveAgent import InteractiveAgent

class Player:
    def __init__(self, type_, name, agent=None):
        self.game = None
        self.num = None
        self.name = name
        self.type = type_
        self.money_dict = self.init_money_dict()
        self.money = sum([k*v for k, v in self.money_dict.items()])
        self.position = 0
        self.turns_in_jail = 0
        self.trains = 0
        self.services = 0
        self.last_dices = 0

        if agent is None:
            agent = InteractiveAgent()
        self.agent =  agent
        self.agent.set_player(self)

    def set_data(self, game, num):
        self.game = game
        self.num = num

    def __eq__(self, other):
        return (self.num == other.num) and (self.name == other.name)

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

        will_buy, amount_h, position_h = self.want_buy_houses()
        if will_buy:
            self.buy_houses(amount_h, position_h)

        self.game.fall_in(self.position)
        return True

    def buy_houses(self, amount, position):
        ### TODO: do it
        ### Check if the player can put houses in the position selected
        pass

    def purchase(self, building):
        self.money -= building.price
        self.game.owners[self.position] = self

    def pay(self, amount):
        ### TODO: Update the money_dict
        self.money -= amount

    def go_to_jail(self):
        self.turns_in_jail = 3
        self.position = 10

    def want_to_buy(self):
        return self.agent.want_to_buy()

    def want_buy_houses(self):
        return self.agent.want_buy_houses()

    def init_money_dict(self):
        return {1: 10, 5: 5, 10: 5, 20: 5, 50: 5, 100: 2, 500: 2}
