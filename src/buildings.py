class Building:
    def __init__(self, name):
        self.name = name

    def __call__(self, player):
        raise NotImplementedError

    def pay(self, owner, player):
        raise NotImplementedError

class VoidBuilding(Building):
    def __call__(self, player):
        pass

    def pay(self, owner, player):
        pass

class JailBuilding(Building):
    def __call__(self, player):
        player.go_to_jail()

    def pay(self, owner, player):
        pass

class LuckyBuilding(Building):
    def __call__(self, player):
        ### TODO: I don't know how to do this
        pass

    def pay(self, owner, player):
        pass

class TrainBuilding(Building):
    def __call__(self, player):
        raise NotImplementedError

    def pay(self, owner, player):
        pass

class ServiceBuilding(Building):
    def __call__(self, player):
        raise NotImplementedError

    def pay(self, owner, player):
        pass

class PropertyBuilding(Building):
    def __init__(self, name, buy, pay):
        super().__init__(name)
        self.buy = buy
        self.pay = pay

    def __call__(self, player):
        if player.want_to_buy():
            2+2
        raise NotImplementedError

    def pay(self, owner, player):
        pass

class TaxesBuilding(Building):
    def __init__(self, name, tax):
        super().__init__(name)
        self.tax = tax

    def pay(self, owner, player):
        pass

    def __call__(self, player):
        player.pay(self.tax)
