# Flashcards Practice Project

A small beginner-friendly Python project for studying with flashcards in the terminal.

## Project Goal

Build a command-line flashcards app that lets you:

- load flashcards from a file
- show one question at a time
- check answers
- keep score

## Beginner-Friendly Plan

### Phase 1: Setup

Start with a tiny working version of the project.

- create `main.py`
- store a few flashcards in `data/flashcards.json`
- print a welcome message
- load the flashcards file

### Phase 2: Core Quiz Loop

Make the app actually quiz the user.

- show one question
- collect the user's answer
- compare it to the correct answer
- print whether the answer was correct

### Phase 3: Score Tracking

Add basic progress tracking.

- count correct answers
- count total questions
- print the final score at the end

### Phase 4: Small Improvements

Once the basics work, improve the experience.

- ignore uppercase vs lowercase differences
- strip extra spaces from answers
- shuffle flashcards before starting
- let the user play again

### Phase 5: Testing

Move simple logic into functions and test it.

- test answer checking
- test flashcard loading
- test score-related behavior

## Suggested File Structure

```text
.
├── README.md
├── .gitignore
├── main.py
├── data/
│   └── flashcards.json
└── tests/
    └── test_main.py
```

## Milestones

1. Make `python main.py` print the loaded flashcards.
2. Add the quiz loop.
3. Add score tracking.
4. Add one or two tests.
5. Refactor only after the app works.

## How To Run

```bash
python main.py
```

## Stretch Ideas

- add categories
- track wrong answers
- save high scores
- let the user add new flashcards
