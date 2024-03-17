class DQNAgent:
    def __init__(self):
        self.player = None
        self.game = None

        self.env = None


    def set_game(self, game):
        self.game = game
        self.env = game.environment
    def set_player(self, player):
        self.player = player

    def want_to_buy(self):
        #Todo: add DQN logic


        # Ask the neuronal network to choose an action

        return False

    def want_buy_houses(self, possible_build):
        #Todo: Change
        return False

    def get_amount_of_houses(self, info):
        #Todo: Change
        return 1

    def notify_cant_buy_bulding(self):
        print("You can't buy the building because you don't have money.")

    def notify_cant_buy_bulding(self):
        print("You can't buy the building because you don't have money.")