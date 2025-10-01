# comprehension_examples.py
# Real-life project examples of Python comprehensions

# 1. Data Cleaning (List Comprehension)
print("\n--- Example 1: Data Cleaning ---")
prices = ["$20", " 30$", "40", "invalid", "$50"]
clean_prices = [
    int(p.replace("$", "").strip())
    for p in prices
    if p.replace("$", "").strip().isdigit()
]
print("Clean Prices:", clean_prices)  # [20, 30, 40, 50]



# 2. Word Frequency (Dictionary Comprehension)
print("\n--- Example 2: Word Frequency ---")
sentence = "python is great and python is popular"
words = sentence.split()
word_count = {word: words.count(word) for word in set(words)}
print("Word Count:", word_count)
# {'is': 2, 'great': 1, 'and': 1, 'popular': 1, 'python': 2}



# 3. Filtering User Data (List Comprehension)
print("\n--- Example 3: Active Users ---")
users = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": False},
    {"name": "Charlie", "active": True},
]
active_users = [user["name"] for user in users if user["active"]]
print("Active Users:", active_users)  # ['Alice', 'Charlie']



# 4. Inverting a Dictionary (Dictionary Comprehension)
print("\n--- Example 4: Invert Dictionary ---")
country_codes = {"US": "United States", "IN": "India", "FR": "France"}
inverted = {v: k for k, v in country_codes.items()}
print("Inverted Dictionary:", inverted)
# {'United States': 'US', 'India': 'IN', 'France': 'FR'}



# 5. Extracting Unique Logs (Set Comprehension)
print("\n--- Example 5: Unique Logs ---")
logs = ["ERROR", "INFO", "DEBUG", "ERROR", "WARNING", "INFO"]
unique_logs = {log for log in logs}
print("Unique Logs:", unique_logs)
# {'ERROR', 'INFO', 'DEBUG', 'WARNING'}
