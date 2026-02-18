"""
Spellathon - Word Puzzle Solver
================================
Find all valid words (4+ letters) from 7 puzzle letters that contain the central letter.
Uses British English dictionary files placed in the 'dictionaries/' folder.
"""

import os
from collections import Counter


# ── Helpers ──────────────────────────────────────────────────────────────────

def load_dictionary(dict_folder: str) -> set[str]:
    """Load all words from every file inside dict_folder into one set."""
    words: set[str] = set()
    if not os.path.isdir(dict_folder):
        print(f"[WARNING] Dictionary folder '{dict_folder}' not found. "
              "Please create it and place your dictionary files inside.")
        return words

    files_loaded = 0
    for filename in os.listdir(dict_folder):
        filepath = os.path.join(dict_folder, filename)
        if not os.path.isfile(filepath):
            continue
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as fh:
                for line in fh:
                    word = line.strip().lower()
                    if word:
                        words.add(word)
            files_loaded += 1
        except Exception as exc:
            print(f"[WARNING] Could not read '{filename}': {exc}")

    if files_loaded == 0:
        print("[WARNING] No dictionary files were loaded. "
              "Place .txt files (one word per line) inside the 'dictionaries/' folder.")
    else:
        print(f"[INFO] Loaded {len(words):,} words from {files_loaded} dictionary file(s).")

    return words


def get_single_letter(prompt: str, existing: list[str] = None) -> str:
    """Prompt the user for a single alphabetic letter, with basic validation."""
    while True:
        raw = input(prompt).strip().lower()
        if len(raw) != 1 or not raw.isalpha():
            print("  → Please enter exactly one letter (a–z).")
            continue
        if existing and raw in existing:
            print(f"  → '{raw.upper()}' has already been entered. Please choose a different letter.")
            continue
        return raw


def get_outer_letters(central: str) -> list[str]:
    """Prompt the user for the 6 surrounding letters (duplicates allowed among them)."""
    print("\nEnter the 6 surrounding letters one at a time.")
    print("(Duplicates among the surrounding letters are allowed.)\n")
    outer: list[str] = []
    for i in range(1, 7):
        letter = get_single_letter(f"  Surrounding letter {i}: ")
        outer.append(letter)
    return outer


def is_valid_word(word: str, central: str, available: Counter) -> bool:
    """
    Return True if the word:
      - is 4 or more letters long
      - contains the central letter at least once
      - uses only letters available in the puzzle (respecting counts)
    """
    if len(word) < 4:
        return False
    if central not in word:
        return False
    word_counter = Counter(word)
    for ch, count in word_counter.items():
        if available[ch] < count:
            return False
    return True


def find_valid_words(dictionary: set[str], central: str, available: Counter) -> list[str]:
    """Return sorted list of all valid words from the dictionary."""
    results = [
        word for word in dictionary
        if is_valid_word(word, central, available)
    ]
    return sorted(results)


def display_results(words: list[str], central: str, all_letters: list[str]) -> None:
    """Print the results in a clean, alphabetical format."""
    letters_display = " ".join(l.upper() for l in all_letters)
    print("\n" + "═" * 50)
    print("  SPELLATHON RESULTS")
    print("═" * 50)
    print(f"  Letters  : {letters_display}")
    print(f"  Centre   : {central.upper()}")
    print("─" * 50)

    if not words:
        print("  No valid words found.")
    else:
        seven_letter = [w for w in words if len(w) == 7]
        other = [w for w in words if len(w) != 7]

        if seven_letter:
            print(f"  ★ Seven-letter word(s): {', '.join(w.upper() for w in seven_letter)}")
            print("─" * 50)

        # Print in columns for readability
        col_width = 18
        cols = 3
        for i, word in enumerate(other):
            end = "\n" if (i + 1) % cols == 0 else ""
            print(f"  {word.upper():<{col_width}}", end=end)
        if len(other) % cols != 0:
            print()  # newline after last partial row

        print("─" * 50)
        print(f"  Total valid words found: {len(words)}")

    print("═" * 50)


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    print("╔══════════════════════════════════════════╗")
    print("║          SPELLATHON  WORD  PUZZLE        ║")
    print("╚══════════════════════════════════════════╝")
    print()
    print("Rules:")
    print("  • Make words of 4 or more letters.")
    print("  • Every word MUST contain the central letter.")
    print("  • A letter may be reused only as many times as it appears in the puzzle.")
    print("  • There should be at least one 7-letter word.")
    print()

    # Load dictionary
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dict_folder = os.path.join(script_dir, "dictionaries")
    dictionary = load_dictionary(dict_folder)

    if not dictionary:
        print("\n[ERROR] Cannot solve without a dictionary. Exiting.")
        return

    print()

    # Get puzzle input
    central = get_single_letter("Enter the CENTRAL letter: ")
    outer = get_outer_letters(central)

    all_letters = [central] + outer
    available = Counter(all_letters)

    # Solve
    valid_words = find_valid_words(dictionary, central, available)

    # Show results
    display_results(valid_words, central, all_letters)

    # Warn if no 7-letter word found (puzzle may be misconfigured)
    seven_letter_words = [w for w in valid_words if len(w) == 7]
    if not seven_letter_words:
        print("\n[NOTE] No 7-letter word was found. "
              "Please double-check the puzzle letters.")

    print()


if __name__ == "__main__":
    main()
