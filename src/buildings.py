class Building:
    def __init__(self, name):
        self.name = name
        self.houses = 0
        self.color = None

    def __call__(self, player):
        raise NotImplementedError

    def pay(self, owner, player):
        raise NotImplementedError

    def get_type(self):
        raise NotImplementedError

class VoidBuilding(Building):
    def __call__(self, player):
        pass

    def get_type(self):
        return "Void"

class JailBuilding(Building):
    def __call__(self, player):
        player.go_to_jail()

    def get_type(self):
        return "Jail"

class LuckyBuilding(Building):
    def __call__(self, player):
        ### TODO: I don't know how to do this
        pass

    def get_type(self):
        return "Lucky"

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

    def get_type(self):
        return "Service"

class TrainBuilding(Building):
    def __init__(self, name):
        super().__init__(name)
        self.price = 200
        self.to_pay = 25

    def __call__(self, player):
        if player.want_to_buy():
            if player.money >= self.price:
                player.purchase(self)
                player.trains += 1
            else:
                player.notify_cant_buy_bulding()

    def pay(self, owner, player):
        to_pay = self.to_pay * (2 ** (owner.trains-1))
        player.pay(to_pay)
        owner.money += to_pay

    def get_type(self):
        return "Train"

class PropertyBuilding(Building):
    def __init__(self, name, price, pay, color, house_price):
        super().__init__(name)
        self.price = price
        self.to_pay = pay
        self.color = color
        self.house_price = house_price

    def __call__(self, player):
        if player.want_to_buy() and player.money >= self.price:
            player.purchase(self)

    def pay(self, owner, player):
        if self.houses == 0:
            to_pay = self.to_pay
        elif self.houses == 1:
            to_pay = self.to_pay * 5
        elif self.houses == 2:
            to_pay = self.to_pay * 15
        elif self.houses == 3:
            to_pay = self.to_pay * 30
        elif self.houses == 4:
            to_pay = self.to_pay * 45
        else:
            to_pay = self.to_pay * 50

        player.pay(to_pay)
        owner.money += to_pay

    def get_type(self):
        return "Property"

class TaxesBuilding(Building):
    def __init__(self, name, tax):
        super().__init__(name)
        self.tax = tax

    def pay(self, owner, player):
        pass

    def __call__(self, player):
        player.pay(self.tax)

    def get_type(self):
        return "Tax"
