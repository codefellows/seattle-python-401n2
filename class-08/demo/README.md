# Demo Notes

- The demo for this class consists of going step by step through the unit and flow tests for version 3 of game.
- Discuss, at the algorithmic level, known solutions from reference code.
- Elicit solutions from class.

## Validate Keepers

- See `test_validate_keepers.py` in reference code.
- The preferred way to `validate keepers` aka `catch cheaters` is to subtract the roll's counter e.g. `Counter(roll)` from the proposed keeper's roll e.g. `Counter(keepers)`.
- This will perform some set math on the 2 counters. See `GameLogic.validate_score` for example.

## Get Scorers

- See `tests\version_3\test_get_scorers.py`in reference code.
- The key idea for `GameLogic.get_scorers` is to remove each of the dice in roll and observe how the score of the roll minus that die is affected.
- If removing a die affects the score then it's a score, otherwise not.

## Flow

- See `tests\version_3\test_flow_3.py` in reference code.

### Cheater / Bad Typer

- See `cheat_and_fix.txt` in reference code.
- Game should give user chance to fix their `keeper` dice in case they just entered them incorrectly.
- Game should loop until keepers are validated.
- Game should allow quitting within the loop.

### Hot Dice

- See `hot_dice.txt` in reference code.
- `Hot dice` are when all dice are exhausted without a zilch.
  - Aka, all dice have scored.
- In that case the turn continues with 6 fresh dice.

### zilch

- See `zilch.txt` in reference code.
- A zilch occurs when a roll has no scoring dice.
- This should be straight forward to implement if version_1 `GameLogic.calculate_score` is functional.

