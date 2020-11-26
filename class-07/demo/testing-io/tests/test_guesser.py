import builtins
from testing_io.guesser import Guesser


def test_help():
    guesser = Guesser()
    actual = guesser.help()
    expected = "Instantiate a Guesser then guess things"
    assert actual == expected

def test_beginners_luck():

    counter = 0

    def mock_print(*args, **kwargs):

        nonlocal counter

        if counter == 0:
            expected = "Step right up and guess my favorite color!"
        else:
            expected = "You got it!"

        counter += 1

        old_print("\n*********")
        old_print(*args, **kwargs)
        old_print("*********")

        actual = args[0]

        assert actual == expected

    def mock_input(*args, **kwargs):
        return "green"


    old_print = builtins.print
    builtins.print = mock_print

    old_input = builtins.input
    builtins.input = mock_input

    guesser = Guesser()

    guesser.guess_fave_color()

    builtins.print = old_print
    builtins.input = old_input

def test_third_times_the_charm():

    prints = [
        "Step right up and guess my favorite color!",
        "Nope, that's not it.",
        "Nope, that's not it.",
        "You got it!",
    ]

    prompts = [
        "What is your guess?",
        "What is your guess?",
        "What is your guess?",
    ]

    responses = [
        "red",
        "blue",
        "green",
    ]

    io_tester = IOTester(prints, prompts, responses)

    guesser = Guesser()

    guesser.guess_fave_color()

    io_tester.exit()


def test_guess_number():
    prints = ["I am thinking of number between 1 and 5","Nope, try again"]
    prompts = ["What number am I thinking of?"]
    responses = ["1"]


    IOTesterWithNums.test(prints, prompts, responses)


class IOTester():
    def __init__(self, prints, prompts, responses):
        self.prints = prints
        self.prompts = prompts
        self.responses = responses

        # self.old_print = builtins.print
        # self.old_input = builtins.input

        # builtins.print = self.mock_print
        # builtins.input = self.mock_input

        print = self.mock_print
        output = self.mock_input

    def mock_print(self, *args, **kwargs):
        expected = self.prints.pop(0)
        actual = args[0]
        assert actual == expected

    def mock_input(self, *args, **kwargs):
        expected = self.prompts.pop(0)
        actual = args[0]
        assert expected == actual
        return self.responses.pop(0)

    def exit(self):
        # builtins.print = self.old_print
        # builtins.input = self.old_input

        assert self.prints == []
        assert self.prompts == []
        assert self.responses == []
class IOTesterWithNums(IOTester):

    def mock_get_random_num(self):
        return self.responses.pop(0)


    @staticmethod
    def test(prints, prompts, responses):
        guesser = Guesser()
        tester = IOTesterWithNums(prints, prompts, responses)
        guesser.guess_random_number()
        tester.exit()
