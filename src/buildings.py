class Building:
    def __init__(self, name):
        self.name = name

class VoidBuilding(Building):
    pass

class JailBuilding(Building):
    pass

class LuckyBuilding(Building):
    pass

class TrainBuilding(Building):
    pass

class ServiceBuilding(Building):
    pass

class PropertyBuilding(Building):
    def __init__(self, name, buy, pay):
        super().__init__(name)
        self.buy = buy
        self.pay = pay

class TaxesBuilding(Building):
    def __init__(self, name, tax):
        super().__init__(name)
        self.tax = tax
