from pytest_bdd import scenario, given, when, then, parsers
from game_of_greed.game_logic import GameLogic


@scenario(
    "calculate_score.feature", "Ones",
)
def test_ones():
    pass


@scenario(
    "calculate_score.feature", "Fives",
)
def test_fives():
    pass


@scenario(
    "calculate_score.feature", "Normals",
)
def test_normals():
    pass


@scenario(
    "calculate_score.feature", "Three Pairs",
)
def test_three_pairs():
    pass


@scenario(
    "calculate_score.feature", "Straight",
)
def test_straight():
    pass


@scenario(
    "calculate_score.feature", "Zilches",
)
def test_zilches():
    pass


@given("I roll <roll>")
def dice_roll(roll):
    return tuple(int(ch) for ch in roll)


@then("I score <score> points")
def should_have_left_cucumbers(dice_roll, score):
    assert GameLogic.calculate_score(dice_roll) == int(score)
