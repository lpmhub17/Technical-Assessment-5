"""CS054 Exercise 2 - Challenge: happy/sad word counter.

Counts how many words in a sentence appear in a happy-word list and in a
sad-word list, then reports the tone of the sentence.

Word lists are plain text files (one word per line). To use a larger public
dataset, replace happy_words.txt / sad_words.txt, e.g. the Hu & Liu opinion
lexicon (positive-words.txt / negative-words.txt).
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))


def load_words(filename):
    with open(os.path.join(HERE, filename), encoding="utf-8") as f:
        return {line.strip().lower() for line in f
                if line.strip() and not line.startswith(";")}


HAPPY_WORDS = load_words("happy_words.txt")
SAD_WORDS = load_words("sad_words.txt")


def tokenize(sentence):
    return re.findall(r"[a-z']+", sentence.lower())


def number_happy(sentence):
    """Return the number of words in sentence found in the happy dataset."""
    return sum(1 for w in tokenize(sentence) if w in HAPPY_WORDS)


def number_sad(sentence):
    """Return the number of words in sentence found in the sad dataset."""
    return sum(1 for w in tokenize(sentence) if w in SAD_WORDS)


def main():
    sentence = input("Enter a sentence: ")
    happy = number_happy(sentence)
    sad = number_sad(sentence)

    print(f"Happy words: {happy}")
    print(f"Sad words: {sad}")

    if happy > sad:
        print("Analysis: The tone of the sentence is happy (positive).")
    elif sad > happy:
        print("Analysis: The tone of the sentence is sad (negative).")
    else:
        print("Analysis: The tone of the sentence is neutral.")


if __name__ == "__main__":
    main()
