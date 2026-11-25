"""CS054 Exercise 2 - Laboratory Activity: Sentiment Analysis with TextBlob.

Asks for 10 sentences, classifies each as Negative / Neutral / Positive
using TextBlob's polarity score, then prints a summary.
"""
from textblob import TextBlob

NUM_SENTENCES = 10

counts = {"Positive": 0, "Neutral": 0, "Negative": 0}

for i in range(1, NUM_SENTENCES + 1):
    sentence = input(f"Enter sentence {i} of {NUM_SENTENCES}: ")
    s = TextBlob(sentence)
    p = s.sentiment.polarity

    # Negative p<0, Neutral p=0, Positive p>0
    if p < 0:
        result = "Negative"
    elif p == 0:
        result = "Neutral"
    elif p > 0 and p <= 1:
        result = "Positive"

    counts[result] += 1
    print(f"  Polarity: {p:.2f} -> {result}\n")

print("=== SUMMARY ===")
print(f"Positive sentences: {counts['Positive']}")
print(f"Neutral sentences : {counts['Neutral']}")
print(f"Negative sentences: {counts['Negative']}")
