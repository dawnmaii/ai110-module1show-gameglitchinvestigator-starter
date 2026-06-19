# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  It looked simple, yet inconsisent design-wise. The hint button didn't look the same as the others. The developer debug log revealed the answer to players,
  located at the top for easy viewing. Not sure how "Normal" difficulty had the greatest range of numbers for guessing, and "Hard" was the next most difficult.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
    1. "Attempts left" text showed different amounts on main screen and sidebar (when opened).
    2. Main screen guess threshold is fixed to "normal" difficulty (1-100) instead of "hard" or "easy" mode when switched via side panel.
    3. Developer debug log is shown by default with no way to turn it off, and it reveals the answer.


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

|               Input              |            Expected Behavior          |          Actual Behavior          |      Console Output / Error       |
|----------------------------------|---------------------------------------|-----------------------------------|-----------------------------------|
| guessed 199                      | input should be rejected with message | hint says "go higher" after guess |             none                  |
| guessed -2                       | input should be rejected with message | hint says "go lower" after guess  |             none                  |
| pressed "new game" after losing  | "game lost" message should be gone    | "game lost" message is still there|             none                  |
| guessed 83                       | input should be accepted w/ result    | no feedback provided w/o hints    |             none                  |
| guessed 34.1                     | input should not be accepted          | input was accepted with hints     |             none                  |
| submitted empty guesses          | "game lost" after max. attempts       | "attempts left" goes to negatives |             none                  |
| pressed "new game" button        | developer debug should reset history  | developer debug retains history   |             none                  |
| changed difficulties             | game should automatically reset       | previous guess history retained   |             none                  |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Claude Code on this project as an extension in VS Code for prompting, and GitHub Copilot's inline suggestions as they arose.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  parse_guess originally did not accept low/high parameters to check that the guess was within the given difficulty, and it also accepted decimal values. AI suggested to have parse_guess take in those parameters to check against the guessed value and eliminate the decimal casting entirely. I verified the result by reading through the changed logic line by line since it was simple enough for me to follow.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  I asked AI about the bug regarding hints not showing up upon user toggle when a guess had been made, and AI suggested to store the hint message in st.session_state and then move the hint display outside the if submit block so the hint doesn't only show upon submit for a given guess. This was not clear to me at first, since the if submit block also had several branches of logic following it. I verified the result by asking clarifying followup questions and then reading the current code to see where I would put the suggested line myself.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  

- Did AI help you design or understand any tests? How?
  

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? This could be a testing habit, a prompting strategy, or a way you used Git.
  

- What is one thing you would do differently next time you work with AI on a coding task?


- In one or two sentences, describe how this project changed the way you think about AI generated code.
