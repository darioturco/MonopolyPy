import numpy as np
from src.player import Player
from src.buildings import VoidBuilding, JailBuilding, PropertyBuilding, LuckyBuilding, TaxesBuilding, TrainBuilding, ServiceBuilding
from src.graphs.plain_text import PlainText

class Monopoly:
    possible_players = ["car", "canyon", "horse", "hat", "ship", "dog", "iron", "barrow"]

    def __init__(self, dices=None, players=None, verbose=False):
        if players is None:
            players = [Player(Monopoly.possible_players[0], "Player 1"), Player(Monopoly.possible_players[1], "Player 2")]
        for i, p in enumerate(players):
            p.set_data(self, i)
        self.players = players
        self.player_index = 0

        if dices is None:
            #dices = Dices(6)
            dices = TrickedDices(6)
        self.dices = dices
        self.building_selector = self.get_building_selector()
        self.owners = {i: None for i in range(len(self.building_selector))}
        self.finish = False
        self.verbose = verbose
        self.render = PlainText(self)

        self.turn = self.players[self.player_index]
        self.turn_count = 0

    def move(self):
        if self.finish:
            if self.verbose:
                print("Game Over.")
        else:
            self.turn_count += 1
            dices = self.dices.throw_dices()
            self.turn.move(dices)
            self.check_if_game_end()
            self.turn = self.next_player()
            self.render.print_status()


    def check_if_game_end(self):
        for p in self.players:
            if p.money < 0:
                self.finish = True
                #Todo: Set info of the finish game

    def fall_in(self, position):
        if self.is_free(position):
            self.building_selector[position](self.turn)

        else:
            owner = self.get_owner_of(position)
            if owner != self.turn:
                self.building_selector[position].pay(owner, self.turn)
    def is_owner_of(self, player, position):
        """ Returns whether the player own the position """
        owner = self.get_owner_of(position)
        return (owner is not None) and (player == owner)

    def get_owner_of(self, position):
        """ Returns the player that purchased the building in the position passed. """
        return self.owners[position]

    def is_free(self, position):
        """ Returns whether a position is already purchased by some player """
        assert (0 <= position < len(self.owners)), "Error position out of range"
        return self.owners[position] is None
    def next_player(self):
        """ Return the next player to move """
        self.player_index = (self.player_index + 1) % len(self.players)
        return self.players[self.player_index]

    def get_position_name(self, position):
        """ Given a position value returns the name(String) of the building in that position """
        return self.building_selector[position].name

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

class TrickedDices:
    def __init__(self, max_value):
        self.max_value = max_value
        self.values = [6, 6]
        self.index = 0

    def throw_dices(self):
        if self.index < len(self.values):
            res = self.values[self.index]
            self.index += 1

        else:
            res = np.sum(np.random.randint(self.max_value, size=2) + 1)

        return res


    def go_out_of_jail(self):
        return np.random.randint(self.max_value) == np.random.randint(self.max_value)