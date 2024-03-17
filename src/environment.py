import numpy as np

class Environment:
    def __init__(self, game):
        self.game = game
        self.actual_state = None
        self.actions = [True, False]    # The actions are to buy the property or don't

    def is_finished(self):
        return self.game.finish

    def create_state(self):
        state = []
        for p in self.game.players:
            state.append(self.create_player_state(p))

        return np.squeeze(state)

    def create_player_state(self, player):
        position = [float(player.position == k) for k, v in self.game.building_selector.items()]
        in_jail = [float(player.turns_in_jail > 0)]
        buildings = [float(self.game.is_owner_of(player, position)) for position in self.game.building_selector.keys()]
        money = [float(i+500 > player.money > i) for i in range(0, 2001, 500)]

        return position + in_jail + buildings + money
    def reset(self):
        self.actual_state = self.create_state()
        return self.actual_state, self.is_finished

    def step(self, action, player):
        ### TODO: Move on the game according with the action
        reward = player.get_reward()
        self.actual_state = self.create_state()
        return self.actual_state, self.actions, self.is_finished(), False, reward
