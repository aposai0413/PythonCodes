from itertools import permutations
from nltk.corpus import words, wordnet
import nltk
import tkinter as tk
from tkinter import scrolledtext

# Ensure the words corpus is downloaded
nltk.download('words')
nltk.download('wordnet')


def load_british_english_words():
    """Load British English words from NLTK corpus."""
    return set(word.lower() for word in words.words())


def get_word_meaning(word):
    """Fetch the meaning of a word using WordNet."""
    synsets = wordnet.synsets(word)
    return synsets[0].definition() if synsets else None


def is_valid_word(word, letter_set, central_letter, word_list):
    """Check if a word is valid based on Spellathon rules."""
    return (
            len(word) >= 4 and
            central_letter in word and
            all(word.count(letter) <= letter_set.count(letter) for letter in word) and
            word in word_list
    )


def generate_spellathon_words(letters, central_letter):
    """Generate valid words for Spellathon given the letters and central letter."""
    letter_set = list(letters.lower())
    central_letter = central_letter.lower()
    dictionary = load_british_english_words()
    valid_words = set()

    for i in range(4, len(letter_set) + 1):  # Words must be at least 4 letters long
        for perm in permutations(letter_set, i):
            word = "".join(perm)
            if is_valid_word(word, letter_set, central_letter, dictionary):
                valid_words.add(word)

    # Ensure at least one seven-letter word exists
    seven_letter_words = [word for word in valid_words if len(word) == 7]
    if not seven_letter_words:
        return "No valid 7-letter word found. Try a different letter set."

    sorted_words = sorted(valid_words)
    return sorted_words, len(sorted_words)


def find_words():
    """Fetch words based on user input and display results in the GUI."""
    letters = letters_entry.get()
    central_letter = central_letter_entry.get()
    words_found, count = generate_spellathon_words(letters, central_letter)

    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    filtered_count = 0

    if isinstance(words_found, str):
        result_text.insert(tk.END, words_found)
    else:
        for word in words_found:
            meaning = get_word_meaning(word)
            if meaning:
                result_text.insert(tk.END, f"{word}: {meaning}\n")
                filtered_count += 1
        result_text.insert(tk.END, f"\nTotal words found with valid meanings: {filtered_count}")

    result_text.config(state=tk.DISABLED)


# Create GUI window
root = tk.Tk()
root.title("Spellathon Solver")
root.geometry("600x400")

# Labels and input fields
tk.Label(root, text="Enter the available letters:").pack()
letters_entry = tk.Entry(root)
letters_entry.pack()

tk.Label(root, text="Enter the central letter:").pack()
central_letter_entry = tk.Entry(root)
central_letter_entry.pack()

# Button to trigger word search
tk.Button(root, text="Find Words", command=find_words).pack()

# Output area
result_text = scrolledtext.ScrolledText(root, width=70, height=15, state=tk.DISABLED)
result_text.pack()

# Run the GUI loop
root.mainloop()
