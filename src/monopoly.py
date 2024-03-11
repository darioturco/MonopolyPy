import numpy as np
from src.player import Player
from src.buildings import VoidBuilding, JailBuilding, PropertyBuilding, LuckyBuilding, TaxesBuilding, TrainBuilding, ServiceBuilding
from src.graphs.plain_text import PlainText
from src.environment import Environment

class Monopoly:
    possible_players = ["car", "canyon", "horse", "hat", "ship", "dog", "iron", "barrow"]

    def __init__(self, dices=None, players=None, verbose=False):
        self.building_selector = self.get_building_selector()
        self.owners = {i: None for i in range(len(self.building_selector))}
        self.colors = self.get_all_colors()

        if players is None:
            players = [Player(Monopoly.possible_players[0], "Player 1"), Player(Monopoly.possible_players[1], "Player 2")]
        for i, p in enumerate(players):
            p.set_data(self, i, self.colors)
        self.players = players
        self.player_index = 0

        if dices is None:
            dices = Dices(6, verbose=True)
            #dices = TrickedDices(6, verbose=False)
        self.dices = dices

        self.environment = Environment(self)

        self.finish = False
        self.verbose = verbose
        self.render = PlainText(self)

        self.turn = self.players[self.player_index]
        self.turn_count = 0

    def move(self):
        """ Move the player that is his turn. """
        if self.finish:
            if self.verbose:
                print("Game Over.")
        else:
            self.turn_count += 1
            self.render.print_status()

            dices = self.dices.throw_dices()
            self.turn.move(dices)
            self.check_if_game_end()
            self.turn = self.next_player()

    def check_if_game_end(self):
        """ Update the finished flag of the game. The game finish when some player have no more money """
        for p in self.players:
            if p.money < 0:
                self.finish = True

    def fall_in(self, position):
        """ Check if the position where a player fall is empty, and make the corresponding action. """
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

    def get_building(self, position):
        """ Given a position value returns the building object in that position """
        return self.building_selector[position]

    def get_position_name(self, position):
        """ Given a position value returns the name(String) of the building in that position """
        return self.get_building(position).name

    def get_positions_buildings_of_player(self, player):
        """ Given a player object, returns the list of the positions of the building that the player owns """
        return [p for p in self.building_selector.keys() if self.get_owner_of(p) == player]

    def play(self):
        """ Start a game and move until the game finish """
        while not self.finish:
            self.move()
        print("Game over.")

    def get_all_colors(self):
        """ Get the set of all colors of the buildings. """
        res = {}
        for _, b in self.building_selector.items():
            if b.color is not None:
                if b.color not in res:
                    res[b.color] = 0
                res[b.color] += 1
        return res

    def get_building_selector(self):
        return  {0: VoidBuilding("Start"),
                  1: PropertyBuilding("Mediterranean Avenue", 60, 2, "Brown", 50),
                  2: LuckyBuilding("Community"),
                  3: PropertyBuilding("Baltic Avenue", 60, 4, "Brown", 50),
                  4: TaxesBuilding("Income Tax", 200),
                  5: TrainBuilding("Reading RR"),
                  6: PropertyBuilding("Oriental Avenue", 100, 6, "Cian", 50),
                  7: LuckyBuilding("Fortune"),
                  8: PropertyBuilding("Vermont Avenue", 100, 6, "Cian", 50),
                  9: PropertyBuilding("Connecticut Avenue", 180, 8, "Cian", 50),
                  10: VoidBuilding("Jail"),
                  11: PropertyBuilding("St Charles Place", 140, 10, "Rose", 100),
                  12: ServiceBuilding("Electric Company"),
                  13: PropertyBuilding("States Avenue", 140, 10, "Rose", 100),
                  14: PropertyBuilding("Virginia Avenue", 160, 12, "Rose", 100),
                  15: TrainBuilding("Pennsylvania RR"),
                  16: PropertyBuilding("St James Place", 180, 14, "Orange", 100),
                  17: LuckyBuilding("Community"),
                  18: PropertyBuilding("Tennessee Avenue", 180, 14, "Orange", 100),
                  19: PropertyBuilding("New York Avenue", 200, 16, "Orange", 100),
                  20: VoidBuilding("Free Stop"),
                  21: PropertyBuilding("Kentucky Avenue", 220, 18, "Red", 150),
                  22: LuckyBuilding("Fortune"),
                  23: PropertyBuilding("Indiana Avenue", 220, 18, "Red", 150),
                  24: PropertyBuilding("Illinois Avenue", 240, 20, "Red", 150),
                  25: TrainBuilding("BO RR"),
                  26: PropertyBuilding("Atlantic Avenue", 260, 22, "Yellow", 150),
                  27: PropertyBuilding("Ventnor Avenue", 260, 22, "Yellow", 150),
                  28: ServiceBuilding("Water Works"),
                  29: PropertyBuilding("Marvin Gardens", 280, 24, "Yellow", 150),
                  30: JailBuilding("Go to Jail"),
                  31: PropertyBuilding("Pacific Avenue", 300, 26, "Green", 200),
                  32: PropertyBuilding("North Carolina Avenue", 300, 26, "Green", 200),
                  33: LuckyBuilding("Community"),
                  34: PropertyBuilding("Pennsylvania Avenue", 320, 28, "Green", 200),
                  35: TrainBuilding("Short Line"),
                  36: LuckyBuilding("Fortune"),
                  37: PropertyBuilding("Park Place", 350, 35, "Blue", 200),
                  38: TaxesBuilding("Luxury Tax", 100),
                  39: PropertyBuilding("Boardwalk", 400, 50, "Blue", 200)}

    def set_state(self, new_state=None):
        if new_state is None:
            new_state = {"turn": 0, # index of the next player to play
                         "players":
                             [{"money": 2000,
                               "position": 0,
                               "buildings": [1, 3],
                               "houses": [0, 0],
                               "turns_in_jail": 0},

                              {"money": 1500,
                               "position": 0,
                               "buildings": [6, 8, 9],
                               "houses": [0, 0, 0],
                               "turns_in_jail": 0}]
                         }

        assert (new_state["turn"] < 0) or (new_state["turn"] >= len(self.players)), "Not valid player index."
        assert (len(new_state['players']) == len(self.players)), "Invalid number of players."
        self.turn = self.players[new_state['turn']]
        self.player_index = new_state['turn']

        for i, player in enumerate(new_state['players']):
            assert player['money'] > 0, "The money of all players need to be positive."
            assert (player['position'] < 0) or (player['position'] >= len(self.building_selector)), "Invalid position."
            assert len(player['position']) != len(player['position']), 'The length of the buildings and the houses of each building is not the same.'

            self.players[i].money = player['money']
            self.players[i].position = player['position']
            self.players[i].turns_in_jail = player['turns_in_jail']

            self.owners = {i: None for i in range(len(self.building_selector))}
            for b, h in zip(player['buildings'], player['houses']):
                self.owners[b] = self.players[i]
                self.get_building(b).houses = h

            player.recalculate_info()

class Dices:
    def __init__(self, max_value, verbose=False):
        self.max_value = max_value
        self.verbose = verbose

    def throw_dices(self):
        res = np.sum(np.random.randint(self.max_value, size=2) + 1)
        if self.verbose:
            print(f"Dices: {res}")
        return res

    def go_out_of_jail(self):
        return np.random.randint(self.max_value) == np.random.randint(self.max_value)

class TrickedDices:
    def __init__(self, max_value, verbose=False):
        self.max_value = max_value
        self.values = [6, 6]
        self.index = 0
        self.verbose = verbose

    def throw_dices(self):
        if self.index < len(self.values):
            res = self.values[self.index]
            self.index += 1

        else:
            res = np.sum(np.random.randint(self.max_value, size=2) + 1)

        return res

    def go_out_of_jail(self):
        return np.random.randint(self.max_value) == np.random.randint(self.max_value)