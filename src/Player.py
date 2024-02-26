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
        self.colors = None

        if agent is None:
            agent = InteractiveAgent()
        self.agent = agent
        self.agent.set_player(self)

    def set_data(self, game, num, colors):
        self.game = game
        self.num = num
        self.agent.set_game(game)
        self.colors = {k: 0 for k in colors.keys()}

    def __eq__(self, other):
        return (other is not None) and (self.num == other.num) and (self.name == other.name)

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
        ### TODO: Check if the player can put houses in the position selected
        building = self.game.get_building(position)
        to_pay = building.house_price * amount
        if self.money >= to_pay:
            building.houses += amount
            self.pay(to_pay)

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

    def get_amount_of_color(self, color):
        return self.colors[color]

    def want_buy_houses(self):
        positions_owned = self.game.get_positions_buildings_of_player(self)
        posible_build = []
        for pos in positions_owned:
            b = self.game.get_building(pos)
            color = b.color
            if (color is not None) and (self.get_amount_of_color(color) == self.game.colors[color]):
                ### TODO: Check the limit of houses
                ### TODO: Check that the player has the necessary money to bui at least one house
                posible_build.append((pos, b.house_price, b.houses))

        can_buy_houses = len(posible_build) > 0
        if can_buy_houses:
            return self.agent.want_buy_houses(posible_build)
        else:
            return False, -1, -1

    def init_money_dict(self):
        return {1: 10, 5: 5, 10: 5, 20: 5, 50: 5, 100: 2, 500: 2}

    def notify_cant_buy_bulding(self):
        return self.agent.notify_cant_buy_bulding()
