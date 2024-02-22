from src.monopoly import Monopoly, Dices

if "__main__" == __name__:
    print("Monopoly...")
    game = Monopoly(Dices(6))
    game.move()