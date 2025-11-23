import re
from collections import Counter


def word_count(text):
    words = re.findall(r"\b\w+\b", text.lower())
    return Counter(words)


text ="""Tester spotted. Panic in Dev team increases. If something works, the tester hasn't touched it yet. Testers don't find bugs—they adopt them"""
print(word_count(text))