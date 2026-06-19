# AI FIXED: Refactored logic into logic_utils.py using Claude


def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    """Return the numeric guessing range for a given difficulty level.

    Args:
        difficulty: One of "Easy", "Normal", or "Hard".

    Returns:
        A tuple (low, high) representing the inclusive guessing range.
        Easy -> (1, 20), Normal -> (1, 50), Hard -> (1, 100).
    """
    if difficulty == "Easy":
        return 1, 20
    elif difficulty == "Normal":
        return 1, 50
    elif difficulty == "Hard":
        return 1, 100


def parse_guess(
    raw: str, low: int, high: int
) -> tuple[bool, int | None, str | None]:
    """Validate raw text input as a whole-number guess within the allowed
    range.

    Rejects empty input, decimals, non-numeric strings, and numbers outside
    the [low, high] boundary before any comparison logic runs.

    Args:
        raw: The raw string entered by the player.
        low: The minimum valid guess (inclusive).
        high: The maximum valid guess (inclusive).

    Returns:
        A tuple (ok, value, error) where:
        - ok (bool): True if the input is valid, False otherwise.
        - value (int | None): The parsed integer if valid, None otherwise.
        - error (str | None): A human-readable error message if invalid,
          None otherwise.
    """
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


def check_guess(guess: int, secret: int) -> tuple[str, str]:
    """Compare a player's guess to the secret number and return an outcome.

    Args:
        guess: The player's guessed integer.
        secret: The secret integer to guess.

    Returns:
        A tuple (outcome, message) where:
        - outcome (str): "Win", "Too High", or "Too Low".
        - message (str): A human-readable hint to display to the player.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    try:
        if guess > secret:
            return "Too High", "📉 Go lower!"
        else:
            return "Too Low", "📈 Go higher!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go lower!"
        return "Too Low", "📈 Go higher!"


def update_score(
    current_score: int, outcome: str, attempt_number: int, difficulty: str
) -> int:
    """Calculate the updated score after a guess.

    Winning awards points that decrease with each attempt (minimum 10).
    Wrong guesses deduct points scaled by difficulty; score cannot go below 0.

    Args:
        current_score: The player's score before this guess.
        outcome: The result of the guess — "Win", "Too High", or "Too Low".
        attempt_number: The 1-based count of valid guesses made so far.
        difficulty: One of "Easy", "Normal", or "Hard".

    Returns:
        The updated score as an integer, never below 0.
    """
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
