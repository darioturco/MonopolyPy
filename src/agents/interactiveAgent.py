class InteractiveAgent:
    def __init__(self):
        self.player = None
        self.game = None

    def set_game(self, game):
        self.game = game
    def set_player(self, player):
        self.player = player

    def want_to_buy(self):
        answer = -1
        while answer == -1:
            building_to_buy = self.game.get_building(self.player.position)
            print(f"Do you wanna buy: {building_to_buy.name}?")
            print(f" Price: {building_to_buy.price}")
            print(f" Your Money: {self.player.money}")
            print(f"1) Yes")
            print(f"2) No")
            answer = input()
            answer = self.parse_answer(answer, [('1', "yes"), ('2', "no")])

            if answer == 0:
                return True
            elif answer == 1:
                return False

        return False

    def want_buy_houses(self, possible_build):
        """ The player decides whether them want to buy some houses. The input possible_build is
            a list of tuple of (position, house_price, amount_of_houses)
            It returns
                    will_buy: boolean that is true if the player want to buy houses
                    amount_h: integer that indicate the amount of houses that the player want to buy
                    position_h: position that indicate the where the houses will be place """
        answer = -1
        while answer == -1:
            print("Wanna buy a house?")
            print(f"1) No")
            for i, pos, house_price, houses in enumerate(possible_build):
                print(f"{i+2}) {self.game.get_position_name(pos)} (Price each house: {house_price} - Houses builded: {houses}) ")

            answer = input()
            answer = self.parse_answer(answer, ['1', 'no'] + [(str(i+2), self.game.get_position_name(pos)) for i, pos, _, _ in enumerate(possible_build) ])
            if answer == 1:
                return False, 0, 0
            elif (answer > 1) and (answer < len(possible_build)):
                houses_to_build = self.get_amount_of_houses(possible_build[answer-2])
                return True, answer, houses_to_build

    def get_amount_of_houses(self, info):
        pos, house_price, amount_of_houses = info
        answer = -1
        max_houses = 5 - amount_of_houses
        while answer == -1:
            print("How many houses want you to buy?")
            for i in range(1, max_houses+1):
                if self.player.money >= house_price * i:
                    print(f"{i}) {i}")

            answer = input()
            answer = self.parse_answer(answer, [(str(i), str(i)) for i in range(1, max_houses+1) if self.player.money >= (house_price * i)])

        return answer + 1

    def parse_answer(self, answer, corrects):
        answer = answer.lower()

        for i, g in enumerate(corrects):
            for a in g:
                if answer == a:
                    return i

        return -1

    def notify_cant_buy_bulding(self):
        print("You can't buy the building because you don't have money.")
