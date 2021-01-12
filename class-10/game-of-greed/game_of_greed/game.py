import sys

from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class Game:
    """Class for Game of Greed application
    """

    def __init__(self, num_rounds=20):

        self.banker = Banker()
        self.num_rounds = num_rounds
        self.round_num = 0

    def play(self, roller=None):
        """Entry point for playing (or declining) a game

        Args:
            roller (function, optional): Allows passing in a custom dice roller function.
                Defaults to None.
        """

        self._roller = roller or GameLogic.roll_dice

        print("Welcome to Game of Greed")

        print("(y)es to play or (n)o to decline")

        response = input("> ")

        if response == "y" or response == "yes":
            self.start_game()
        else:
            self.decline_game()

    def decline_game(self):
        print("OK. Maybe another time")

    def start_game(self):

        self.round_num = 1

        while self.round_num <= self.num_rounds:

            self.start_round(self.round_num)

            self.round_num += 1

            print(f"Total score is {self.banker.balance} points")

        self.quit_game()

    def quit_game(self):

        print(f"Thanks for playing. You earned {self.banker.balance} points")

        sys.exit()

    def start_round(self, round, num_dice=6):

        print(f"Starting round {round}")

        round_score = 0

        while True:

            roll = self.roll_dice(num_dice)

            if self.got_zilch(roll):
                break

            keepers = self.handle_keepers(roll)

            print("(r)oll again, (b)ank your points or (q)uit:")

            roll_again_response = input("> ")

            if roll_again_response == "q":

                self.quit_game()

                return

            elif roll_again_response == "b":

                round_score = self.banker.bank()

                break

            else:

                num_dice -= len(keepers)

                if num_dice == 0:

                    num_dice = 6

        print(f"You banked {str(round_score)} points in round {round}")

    def handle_keepers(self, roll):

        while True:
            print("Enter dice to keep, or (q)uit:")

            keeper_string = input("> ")

            if keeper_string.startswith("q"):
                self.quit_game()

            keepers = self.gather_keepers(roll, keeper_string)

            roll_score = self.calculate_score(keepers)

            if roll_score == 0:
                print("Must keep at least one scoring dice")
            else:
                break

        self.banker.shelf(roll_score)

        num_dice_remaining = len(roll) - len(keepers)

        print(
            f"You have {self.banker.shelved} unbanked points and {num_dice_remaining} dice remaining"
        )

        return keepers

    def roll_dice(self, num):

        print(f"Rolling {num} dice...")

        roll = self._roller(num)

        print("*** " + " ".join([str(i) for i in roll]) + " ***")

        return roll

    def got_zilch(self, roll):

        initial_score = self.calculate_score(roll)

        if initial_score == 0:

            width = 40
            print("*" * width)
            print("**" + "Zilch!!! Round over".center(width - 4) + "**")
            print("*" * width)

            self.banker.clear_shelf()

            return True

        return False

    def calculate_score(self, roll):
        return GameLogic.calculate_score(roll)

    def _convert_keepers(self, keeper_string):

        return [int(ch) for ch in keeper_string if ch.isdigit()]

    def gather_keepers(self, roll, keeper_string):

        keepers = self._convert_keepers(keeper_string)

        while not GameLogic.validate_keepers(roll, keepers):
            print("Cheater!!! Or possibly made a typo...")
            print("*** " + " ".join([str(i) for i in roll]) + " ***")
            print("Enter dice to keep, or (q)uit:")
            keeper_string = input("> ")
            if keeper_string.startswith("q"):
                self.quit_game()

            keepers = self._convert_keepers(keeper_string)

        return keepers


def clear():
    # stretch goal to allow user to clear terminal mid game

    # os.system("cls" if os.name == "nt" else "clear")
    pass


if __name__ == "__main__":

    rolls = [(1, 1, 3, 3, 6, 6)]

    def roller(num):
        if rolls:
            return rolls.pop(0)

        return GameLogic.roll_dice(num)

    game = Game()
    game.play(roller=roller)
