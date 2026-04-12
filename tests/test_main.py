from pathlib import Path

from main import is_correct_answer, load_flashcards, normalize_answer


def test_normalize_answer_removes_spaces_and_lowercases() -> None:
    assert normalize_answer("  Paris  ") == "paris"


def test_is_correct_answer_ignores_case_and_spaces() -> None:
    assert is_correct_answer("  paris ", "Paris")


def test_load_flashcards_returns_cards() -> None:
    flashcards = load_flashcards(Path("data/flashcards.json"))
    assert len(flashcards) >= 1
    assert "question" in flashcards[0]
    assert "answer" in flashcards[0]
