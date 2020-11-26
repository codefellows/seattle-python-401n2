


import random

class Guesser:
    def __init__(self):
        self.fave_color = "green"


    def help(self):
        print("Instantiate a Guesser then guess things")

    def greet(self):
        name = input("What is your name? ")

        print(f"Hi, {name}. Let's get to guessing!")

    def guess_fave_color(self):
        print("Step right up and guess my favorite color!")
        response = input("What is your guess?")
        while response != self.fave_color:
            print("Nope, that's not it.")
            response = input("What is your guess?")

        print("You got it!")

    def guess_random_number(self):
        num = self.get_random_num()

        print("I am thinking of number between 1 and 5")

        response = int(input("What number am I thinking of?"))

        while response != num:
            print("Nope, try again")
            response = int(input("What number am I thinking of?"))

        print("You got it!")


    def get_random_num(self):
        return random.randint(1,5)


if __name__ == "__main__":
    g = Guesser()
    # g.help()
    g.greet()
    # g.guess_random_number()






