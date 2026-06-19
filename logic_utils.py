# AI FIXED: Refactored logic into logic_utils.py using Claude

# FIXED: difficulty ranges were not being applied correctly
def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    elif difficulty == "Normal":
        return 1, 50
    elif difficulty == "Hard":
        return 1, 100

# AI FIXED: checks input for whole number within guessing threshold before guessing
def parse_guess(raw: str, low: int, high: int):
    if raw is None or raw == "":
        return False, None, "Enter a guess."
    if "." in raw:
        return False, None, "Enter a whole number."
    try:
        value = int(raw)
    except Exception:
        return False, None, "That is not a number."
    if value < low or value > high:
        return False, None, f"Guess must be between {low} and {high}."
    return True, value, None


def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!"
    try:
        if guess > secret:
            return "Too High", "📈 Go HIGHER!"
        else:
            return "Too Low", "📉 Go LOWER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📈 Go HIGHER!"
        return "Too Low", "📉 Go LOWER!"

# AI FIXED: points earned/deducted now corresponds to difficulty settings and attempt number, negative points not possible
def update_score(current_score: int, outcome: str, attempt_number: int, difficulty: str):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        if difficulty == "Easy":
            deduction = 2
        elif difficulty == "Normal":
            deduction = attempt_number * 2
        else:
            deduction = attempt_number * 5
        return max(0, current_score - deduction)

    return current_score
