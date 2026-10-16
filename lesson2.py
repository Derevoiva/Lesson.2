"""Corrected Python 3 implementations of the five Lesson 2 exercises.

The original course submission is preserved in the repository.
Run: python lesson2.py
"""
from __future__ import annotations
from bisect import bisect_right


def element_types(items: list[object]) -> list[str]:
    """Return readable type names for every input element."""
    return [type(item).__name__ for item in items]


def swap_neighbors(items: list[object]) -> list[object]:
    """Swap consecutive pairs while preserving an unmatched last element."""
    result = items.copy()
    for i in range(0, len(result) - 1, 2):
        result[i], result[i + 1] = result[i + 1], result[i]
    return result


def season_for_month(month: int) -> str:
    """Return a season for months 1-12."""
    if not 1 <= month <= 12:
        raise ValueError("Month must be between 1 and 12")
    seasons = ("winter", "spring", "summer", "autumn")
    month_to_season = {
        12: "winter", 1: "winter", 2: "winter",
        3: "spring", 4: "spring", 5: "spring",
        6: "summer", 7: "summer", 8: "summer",
        9: "autumn", 10: "autumn", 11: "autumn",
    }
    assert month_to_season[month] in seasons
    return month_to_season[month]


def numbered_words(text: str, max_length: int = 10) -> list[str]:
    """Number the words, truncating each word independently."""
    if max_length < 1:
        raise ValueError("max_length must be positive")
    return [f"{index}. {word[:max_length]}" for index, word in enumerate(text.split(), 1)]


def insert_rating(ratings: list[int], value: int) -> list[int]:
    """Insert a positive integer in descending order after equal values."""
    if value < 1 or any(item < 1 for item in ratings):
        raise ValueError("Ratings must contain positive integers")
    if any(a < b for a, b in zip(ratings, ratings[1:])):
        raise ValueError("Ratings must already be sorted in descending order")
    result = ratings.copy()
    # Bisect on the negated values gives descending order with equal values first.
    positions = [-item for item in result]
    insertion_index = bisect_right(positions, -value)
    result.insert(insertion_index, value)
    return result


def main() -> None:
    print("Lesson 2 — corrected exercises (1–5)")
    choice = input("Choose exercise: ").strip()
    try:
        if choice == "1":
            print(element_types([6, None, -27, "True", True, 7.1]))
        elif choice == "2":
            count = int(input("Number of elements: "))
            if count < 0:
                raise ValueError("Count must be non-negative")
            items = [input(f"Element {i + 1}: ") for i in range(count)]
            print(swap_neighbors(items))
        elif choice == "3":
            print(season_for_month(int(input("Month (1–12): "))))
        elif choice == "4":
            print(*numbered_words(input("Words: ")), sep="\n")
        elif choice == "5":
            ratings = [7, 5, 3, 3, 2]
            while True:
                answer = input("Positive rating (blank to stop): ").strip()
                if not answer:
                    break
                ratings = insert_rating(ratings, int(answer))
                print(ratings)
        else:
            print("Unknown exercise")
    except ValueError as error:
        print(f"Input error: {error}")


if __name__ == "__main__":
    main()
