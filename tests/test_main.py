from app.main import greet, calculate_score

def test_greet_returns_greeting():
    assert greet("World") == "Hello, World!"

def test_total_score():
    assert calculate_score([100]) == 100

def test_roll():
    assert calculate_score([3, 3, 3]) == 9

def test_spare():
    rolls = [5, 5, 3] + [0] * 17
    assert calculate_score(rolls) == 16

def test_strike():
    rolls = [10, 3, 4] + [0] * 16
    assert calculate_score(rolls) == 24