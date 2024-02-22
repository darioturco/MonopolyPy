class Building:
    def __init__(self, name):
        self.name = name
        self.houses = 0

    def __call__(self, player):
        raise NotImplementedError

    def pay(self, owner, player):
        raise NotImplementedError

class VoidBuilding(Building):
    def __call__(self, player):
        pass

class JailBuilding(Building):
    def __call__(self, player):
        player.go_to_jail()

class LuckyBuilding(Building):
    def __call__(self, player):
        ### TODO: I don't know how to do this
        pass

class ServiceBuilding(Building):
    def __init__(self, name):
        super().__init__(name)
        self.price = 150

    def __call__(self, player):
        if player.want_to_buy() and player.money >= self.price:
            player.purchase(self)
            player.services += 1

    def pay(self, owner, player):
        if owner.services == 1:
            to_pay = player.last_dices * 4
        elif owner.services == 2:
            to_pay = player.last_dices * 10
        else:
            to_pay = 0

        player.pay(to_pay)
        owner.money += to_pay

class TrainBuilding(Building):
    def __init__(self, name):
        super().__init__(name)
        self.price = 200
        self.pay = 25

    def __call__(self, player):
        if player.want_to_buy() and player.money >= self.price:
            player.purchase(self)
            player.trains += 1

    def pay(self, owner, player):
        to_pay = self.price * (2 ** (owner.trains-1))
        player.pay(to_pay)
        owner.money += to_pay

class PropertyBuilding(Building):
    def __init__(self, name, price, pay):
        super().__init__(name)
        self.price = price
        self.pay = pay

    def __call__(self, player):
        if player.want_to_buy() and player.money >= self.price:
            player.purchase(self)

    def pay(self, owner, player):
        if self.houses == 0:
            to_pay = self.pay
        elif self.houses == 1:
            to_pay = self.pay * 5
        elif self.houses == 2:
            to_pay = self.pay * 15
        elif self.houses == 3:
            to_pay = self.pay * 30
        elif self.houses == 4:
            to_pay = self.pay * 45
        else:
            to_pay = self.pay * 50

        player.pay(to_pay)
        owner.money += to_pay

class TaxesBuilding(Building):
    def __init__(self, name, tax):
        super().__init__(name)
        self.tax = tax

    def pay(self, owner, player):
        pass

    def __call__(self, player):
        player.pay(self.tax)
