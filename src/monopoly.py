import numpy as np
from src.player import Player
from src.buildings import VoidBuilding, JailBuilding, PropertyBuilding, LuckyBuilding, TaxesBuilding, TrainBuilding, ServiceBuilding

class Monopoly:
    possible_players = ["car", "canyon", "horse", "hat", "ship", "dog", "iron", "barrow"]



    def __init__(self, dices=None, players=None):
        if players is None:
            players = [Player(Monopoly.possible_players[0]), Player(Monopoly.possible_players[1])]
        for i, p in enumerate(players):
            p.set_data(self, i)
        self.players = players
        self.player_index = 0

        self.dices = dices
        self.building_selector = self.get_building_selector()
        self.buildings_purchased = {i: None for i in range(len(self.building_selector))}
        self.finish = False

        self.turn = self.players[self.player_index]

    def move(self):
        dices = self.dices.throw_dices()
        self.turn.move(dices)

        self.turn = self.next_player()

    def fall_in(self, position):
        if self.is_free(position):
            self.building_selector[position](self.turn)

        owner = self.get_owner_of(position)
        if not owner != self.turn:
            self.building_selector[position].pay(self.turn)

    def get_owner_of(self, position):
        """ Returns the player that purchased the building in the position passed. It assumes that the building has owner """
        return self.buildings_purchased[position]

    def is_free(self, position):
        ### Todo: Check that position is in range
        return self.buildings_purchased[position] is None
    def next_player(self):
        self.player_index = (self.player_index + 1) % len(self.players)
        return self.players[self.player_index]

    def get_building_selector(self):
        return  {0: VoidBuilding("Start"),
                  1: PropertyBuilding("Mediterranean Avenue", 60, 2),
                  2: LuckyBuilding("Community"),
                  3: PropertyBuilding("Baltic Avenue", 60, 4),
                  4: TaxesBuilding("Income Tax", 200),
                  5: TrainBuilding("Reading RR"),
                  6: PropertyBuilding("Oriental Avenue", 100, 6),
                  7: LuckyBuilding("Fortune"),
                  8: PropertyBuilding("Vermont Avenue", 100, 6),
                  9: PropertyBuilding("Connecticut Avenue", 180, 8),
                  10: VoidBuilding("Jail"),
                  11: PropertyBuilding("St Charles Place", 140, 10),
                  12: ServiceBuilding("Electric Company"),
                  13: PropertyBuilding("States Avenue", 140, 10),
                  14: PropertyBuilding("Virginia Avenue", 160, 12),
                  15: TrainBuilding("Pennsylvania RR"),
                  16: PropertyBuilding("St James Place", 180, 14),
                  17: LuckyBuilding("Community"),
                  18: PropertyBuilding("Tennessee Avenue", 180, 14),
                  19: PropertyBuilding("New York Avenue", 200, 16),
                  20: VoidBuilding("Free Stop"),
                  21: PropertyBuilding("Kentucky Avenue", 220, 18),
                  22: LuckyBuilding("Fortune"),
                  23: PropertyBuilding("Indiana Avenue", 220, 18),
                  24: PropertyBuilding("Illinois Avenue", 240, 20),
                  25: TrainBuilding("BO RR"),
                  26: PropertyBuilding("Atlantic Avenue", 260, 22),
                  27: PropertyBuilding("Ventnor Avenue", 260, 22),
                  28: ServiceBuilding("Water Works"),
                  29: PropertyBuilding("Marvin Gardens", 280, 24),
                  30: JailBuilding("Go to Jail"),
                  31: PropertyBuilding("Pacific Avenue", 300, 26),
                  32: PropertyBuilding("North Carolina Avenue", 300, 26),
                  33: LuckyBuilding("Community"),
                  34: PropertyBuilding("Pennsylvania Avenue", 320, 28),
                  35: TrainBuilding("Short Line"),
                  36: LuckyBuilding("Fortune"),
                  37: PropertyBuilding("Park Place", 350, 35),
                  38: TaxesBuilding("Luxury Tax", 100),
                  39: PropertyBuilding("Boardwalk", 400, 50)}

class Dices:
    def __init__(self, max_value):
        self.max_value = max_value

    def throw_dices(self):
        return np.sum(np.random.randint(self.max_value, size=2) + 1)

    def go_out_of_jail(self):
        return np.random.randint(self.max_value) == np.random.randint(self.max_value)