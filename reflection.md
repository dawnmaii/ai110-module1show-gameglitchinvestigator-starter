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
  I had AI explain to me what was used to fix the bug and why, along with clarifying questions to ensure I understood the fix. Then I ran the game again and tested with different inputs to ensure the big fix didn't create more bugs. I tried to do this every few major changes before testing the app as a whole.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  I ran the tests testing the check_guess function via pytest on Claude, and Claude actually pointed out a few bugs in both my tests and the code, which I then fixed manually. It showed me that even with AI assistance, code can still be buggy and needs to be manually reviewed.

- Did AI help you design or understand any tests? How?
  GitHub CoPilot helped me design my tests; after I imported the functions from logic_utils.py, pressing the Tab key automatically gave me potential tests for me to use in validating the I/O of these functions. I reviewed them line-by-line before pressing Tab, it was cool to see. It even gave me cases I never really considered. Typing out test names automatically gave me the recommended code based on the test name.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  So every time a Streamlit app is active, it is currently in a "session". A Streamlit session state consists of the properties of a given session, for instance what the screen presents at the beginning or what buttons are turned on or off. Properties can change value, or "state" at any given time during the current session. Some of them can "rerun" the session, forcing Streamlit to run the script from top to bottom.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? This could be a testing habit, a prompting strategy, or a way you used Git.
  One strategy I would like to get into the habit of using is manually going through the code to comment todos, then attempting manual fixes with my working knowledge whenever possible before using AI to "fill in the blanks" and help me reason about how I would fix similar issues in the future or learn about the codebase and the libraries used. I didn't know about Streamlit before, but now I have working knowledge of it and that's pretty cool to me.

- What is one thing you would do differently next time you work with AI on a coding task?
  I would ask it to go through the codebase initially with me first and ask it clarifying questions on what's being used and why, instead of learning along the way as I fix bugs. I do pride myself in being able to do all this with minimal AI use.

- In one or two sentences, describe how this project changed the way you think about AI-generated code.
  It's not as bad as I thought, provided you know what you want to ask and why you're asking said question with what objective. You have to be thorough with your thought process, but at the same time I really don't want to rely on it because it's that powerful. Slightly impressed and scared.