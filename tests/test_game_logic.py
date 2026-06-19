from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

# Tests generated with Copilot inline suggestions and reviewd by Claude via running the file from root

# testing check_guess function
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win" and result[1] == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Go HIGHER!"
    result = check_guess(60, 50)
    assert result[0] == "Too High" and result[1] == "📈 Go HIGHER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Go LOWER!"
    result = check_guess(40, 50)
    assert result[0] == "Too Low" and result[1] == "📉 Go LOWER!"


# testing get_range_for_difficulty function
def test_easy_range():
    # On Easy difficulty, range should be 1 to 20
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20

def test_normal_range():
    # On Normal difficulty, range should be 1 to 50
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 50

def test_hard_range():
    # On Hard difficulty, range should be 1 to 100
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 100


# testing parse_guess function
def test_parse_guess_valid():
    # Valid guess within range should return True and the integer value
    result = parse_guess("25", 1, 100)
    assert result == (True, 25, None)

def test_parse_guess_non_integer():
    # Non-integer input should return False and an error message
    result = parse_guess("abc", 1, 100)
    assert result == (False, None, "That is not a number.")

def test_parse_guess_decimal():
    # Decimal input should return False and an error message
    result = parse_guess("25.5", 1, 100)
    assert result == (False, None, "Enter a whole number.")

def test_parse_guess_out_of_range():
    # Guess outside of range should return False and an error message
    result = parse_guess("150", 1, 100)
    assert result == (False, None, "Guess must be between 1 and 100.")

def test_parse_guess_empty():
    # Empty input should return False and an error message
    result = parse_guess("", 1, 100)
    assert result == (False, None, "Enter a guess.")

def test_parse_guess_negative():
    # Negative input should return False and an error message
    result = parse_guess("-25", 1, 100)
    assert result == (False, None, "Guess must be between 1 and 100.")

def test_parse_guess_large_number():
    # Very large number input should return False and an error message
    result = parse_guess("1000000", 1, 100)
    assert result == (False, None, "Guess must be between 1 and 100.")


# testing update_score function
def test_update_score_win():
    # Winning on the first attempt should give 80 points on Normal difficulty
    score = update_score(0, "Win", 1, "Normal")
    assert score == 80 

def test_update_score_too_high_normal():
    # On Normal difficulty, a wrong guess on the 2nd attempt should deduct 4 points
    score = update_score(100, "Too High", 2, "Normal")
    assert score == 96

def test_update_score_too_low_normal():
    # On Normal difficulty, a wrong guess on the 4th attempt should deduct 8 points
    score = update_score(100, "Too Low", 4, "Normal")
    assert score == 92

def test_update_score_win_late_attempt():
    # Winning on the 10th attempt should give 10 points on Hard difficulty
    score = update_score(0, "Win", 10, "Hard")
    assert score == 10

def test_update_score_too_high_easy():
    # On Easy difficulty, a wrong guess should deduct 2 points
    score = update_score(100, "Too High", 1, "Easy")
    assert score == 98

def test_update_score_too_high_hard():
    # On Hard difficulty, a wrong guess on the 5th attempt should deduct 25 points
    score = update_score(100, "Too High", 5, "Hard")
    assert score == 75

def test_update_score_too_low_hard():
    # On Hard difficulty, a wrong guess on the 3rd attempt should deduct 15 points
    score = update_score(100, "Too Low", 3, "Hard")
    assert score == 85

def test_update_score_no_negative():
    # Score should not go negative
    score = update_score(5, "Too High", 10, "Hard")
    assert score == 0

def test_update_score_no_change_on_invalid_outcome():
    # If outcome is not "Win", "Too High", or "Too Low", score should not change
    score = update_score(50, "Invalid Outcome", 1, "Normal")
    assert score == 50 