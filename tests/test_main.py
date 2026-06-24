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

def test_perfect_game():
    rolls = [10] * 12
    assert calculate_score(rolls) == 300   

def test_gutter_game():
    # all zeros
    rolls = [0] * 20
    assert calculate_score(rolls) == 0

def test_turkey_three_strikes():  
    # Three strikes in a row 
    rolls = [10, 10, 10] + [0] * 14
    assert calculate_score(rolls) == 60     

def test_tenth_frame_spare_with_strike(): 
    # spare in the 10th frame,
    rolls = [0] * 18 + [5, 5, 10]
    assert calculate_score(rolls) == 20    