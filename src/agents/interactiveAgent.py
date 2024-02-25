class InteractiveAgent:
    def __init__(self):
        self.player = None

    def set_player(self, player):
        self.player = player

    def want_to_buy(self):
        print(f"Do you wanna buy...") # TODO: Complete
        return True

    def want_buy_houses(self):
        """ The player decides whether them want to buy some houses. It returns
                    will_buy: boolean that is true if the player want to buy houses
                    amount_h: integer that indicate the amount of houses that the player want to buy
                    position_h: position that indicate the where the houses will be place """
        ### TODO: delegate to the decision module of the player
        return False, 0, 0
