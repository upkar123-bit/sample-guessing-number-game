import pytest
from game import NumberGuessGame

def test_guess_too_low():
    game = NumberGuessGame(1, 10)
    game.target = 7
    assert game.guess(3) == "Too low!"

def test_guess_too_high():
    game = NumberGuessGame(1, 10)
    game.target = 7
    assert game.guess(9) == "Too high!"

def test_guess_correct():
    game = NumberGuessGame(1, 10)
    game.target = 5
    result = game.guess(5)
    assert "Correct!" in result
    assert game.attempts == 1

def test_guess_out_of_range():
    game = NumberGuessGame(1, 10)
    result = game.guess(20)
    assert "between" in result
