# Spellathon – Word Puzzle Solver

A Python command-line tool that solves the **Spellathon** word puzzle using your own British English dictionary files.

---

## 📋 Rules

- Make words of **4 or more letters**.
- Every word **must contain the central letter**.
- A letter may be reused only **as many times as it appears** in the puzzle (7 letters total).
- There should be **at least one 7-letter word** in the solution.
- Plurals, foreign words, and proper names are **not** allowed.
- Reference: **British English Dictionary**.

---

## 📁 Project Structure

```
Spellathon/
│
├── spellathon.py        ← Main program
├── README.md            ← This file
│
└── dictionaries/        ← Place your dictionary files here
    ├── words1.txt
    ├── words2.txt
    └── ...              (any number of .txt files)
```

---

## 📖 Dictionary Setup

1. Place one or more dictionary files inside the `dictionaries/` folder.
2. Each file should have **one word per line**, plain text (`.txt`), UTF-8 encoded.
3. You can organise them however you like — the program loads **all files** in the folder automatically.

Example `dictionaries/british_english.txt`:
```
able
about
above
...
```

---

## ▶️ How to Run

Make sure you have **Python 3.10+** installed.

```bash
cd Spellathon
python spellathon.py
```

### Example session

```
╔══════════════════════════════════════════╗
║          SPELLATHON  WORD  PUZZLE        ║
╚══════════════════════════════════════════╝

Rules:
  • Make words of 4 or more letters.
  • Every word MUST contain the central letter.
  • A letter may be reused only as many times as it appears in the puzzle.
  • There should be at least one 7-letter word.

[INFO] Loaded 58,109 words from 1 dictionary file(s).

Enter the CENTRAL letter: g
Enter the 6 surrounding letters one at a time.

  Surrounding letter 1: r
  Surrounding letter 2: a
  Surrounding letter 3: n
  Surrounding letter 4: i
  Surrounding letter 5: t
  Surrounding letter 6: e

══════════════════════════════════════════════════
  SPELLATHON RESULTS
══════════════════════════════════════════════════
  Letters  : G R A N I T E
  Centre   : G
  ──────────────────────────────────────────────
  ★ Seven-letter word(s): GRANITE, INGRATE
  ──────────────────────────────────────────────
  EARN              GAIT              GAIN
  ...
  ──────────────────────────────────────────────
  Total valid words found: 42
══════════════════════════════════════════════════
```

---

## ⚙️ Requirements

- Python **3.10** or later (uses `set[str]` and `list[str]` type hints natively).
- No third-party packages required — uses only the standard library.

---

## 🛠️ Notes

- The program validates each letter input (single alphabetic character only).
- Duplicate letters among the 6 surrounding letters are **allowed** (e.g., two S's).
- The central letter must be unique from the surrounding letters.
- If no 7-letter word is found, the program warns you to double-check the puzzle.
