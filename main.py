import json
from pathlib import Path
from typing import Dict, List


FLASHCARDS_PATH = Path("data/flashcards.json")


def load_flashcards(path: Path) -> List[Dict[str, str]]:
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def normalize_answer(answer: str) -> str:
    return answer.strip().lower()


def is_correct_answer(user_answer: str, correct_answer: str) -> bool:
    return normalize_answer(user_answer) == normalize_answer(correct_answer)


def run_quiz() -> None:
    flashcards = load_flashcards(FLASHCARDS_PATH)
    score = 0

    print("Welcome to Flashcards Practice!")
    print()

    for card in flashcards:
        print(f"Question: {card['question']}")
        user_answer = input("Your answer: ")

        if is_correct_answer(user_answer, card["answer"]):
            print("Correct!")
            score += 1
        else:
            print(f"Not quite. Correct answer: {card['answer']}")

        print()

    print(f"Final score: {score}/{len(flashcards)}")


if __name__ == "__main__":
    run_quiz()
