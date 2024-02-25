class PlainText:
    def __init__(self, game):
        self.game = game

    def print_status(self):
        print(f"\n---------------------------------------")
        print(f"Turn of: {self.game.turn.name}\n")
        for p in self.game.players:
            print(f"{p.name}: ")
            print(f" Position: {self.game.get_position_name(p.position)} ({p.position}) ")
            print(f" Money: {p.money} ")
            print(f" Turns left in jail: {max(p.turns_in_jail, 0)} ")
            print(f" Buildings: ")
            for k, b in self.game.building_selector.items():
                if self.game.is_owner_of(p, k):
                    print(f"   {b.name} ({b.houses})")

        print("\n")