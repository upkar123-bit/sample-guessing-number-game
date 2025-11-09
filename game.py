import random

class NumberGuessGame:
    def __init__(self, lower=1, upper=100):
        self.lower = lower
        self.upper = upper
        self.target = random.randint(lower, upper)
        self.attempts = 0

    def guess(self, number: int) -> str:
        """Takes a guess and returns feedback."""
        if not (self.lower <= number <= self.upper):
            return f"Please guess a number between {self.lower} and {self.upper}."

        self.attempts += 1
        if number < self.target:
            return "Too low!"
        elif number > self.target:
            return "Too high!"
        else:
            return f"Correct! You found the number in {self.attempts} attempts."
