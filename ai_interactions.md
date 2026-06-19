# AI Interactions Log

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case |          Prompt Used         |        AI-Suggested Test       | Did It Pass? |                                 Your Reasoning                                    |
|-----------|------------------------------|--------------------------------|--------------|-----------------------------------------------------------------------------------|
| decimals  | typed in test_parse_guess... | test_parse_guess_decimal()     |     yes      | Previously, user was instructed to guess a number, so decimals were a possibility.|
| strings   | tests were autocompleted as  | test_parse_guess_non_integer() |     yes      | You never know what the user might do, so I added it just in case.                |
| negatives | inline suggestions (tab key) | test_parse_guess_negative()    |     yes      | When first playing the game, I actually used negative numbers as guesses.         |
| empty     | and verified manually        | test_parse_guess_empty()       |     yes      | Users can guess accidentally w/ an empty input; shouldn't be counted against them.|
---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
I would like to add professional-grade docstrings to every function in logic_utils.py.

Review my code in logic_utils.py for PEP 8 style compliance and explain how it could comply.

```

**Linting output before:**

```
logic_utils.py:12:80: E501 line too long (83 > 79 characters)
logic_utils.py:13:1: E302 expected 2 blank lines, found 1
logic_utils.py:44:80: E501 line too long (122 > 79 characters)
logic_utils.py:45:1: E302 expected 2 blank lines, found 1
logic_utils.py:45:80: E501 line too long (89 > 79 characters)

```

**Changes applied:**

1. Wrapped docstring lines and function definitions to the next line, such that no line exceeded 79 characters.