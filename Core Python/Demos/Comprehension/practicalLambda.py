# lambda_map_filter_reduce_realworld.py
# Real-world project examples using lambda, map, filter, reduce

from functools import reduce

# 1. Data Cleaning in ETL Pipelines
print("\n--- Example 1: Data Cleaning ---")
raw_names = [" Alice ", "bob", "", "CHARLIE", None, "david "]
clean_names = list(
    map(lambda x: x.strip().capitalize(), filter(lambda n: n and n.strip(), raw_names))
)
print("Clean Names:", clean_names)
# ['Alice', 'Bob', 'Charlie', 'David']



# 2. Log File Analysis (Filtering Errors)
print("\n--- Example 2: Log File Analysis ---")
logs = [
    "INFO: User logged in",
    "ERROR: Database not found",
    "DEBUG: API response received",
    "ERROR: Timeout occurred",
    "INFO: User logged out",
]
error_logs = list(filter(lambda log: log.startswith("ERROR"), logs))
print("Error Logs:", error_logs)
# ['ERROR: Database not found', 'ERROR: Timeout occurred']



# 3. Financial Transactions (Reduce for Aggregation)
print("\n--- Example 3: Financial Transactions ---")
transactions = [
    {"amount": 1000, "type": "credit"},
    {"amount": 200, "type": "debit"},
    {"amount": 500, "type": "credit"},
    {"amount": 100, "type": "debit"},
]
balance = reduce(
    lambda acc, t: acc + t["amount"] if t["type"] == "credit" else acc - t["amount"],
    transactions,
    0,
)
print("Final Balance:", balance)  # 1200



# 4. API Data Transformation
print("\n--- Example 4: API Data Transformation ---")
api_response = [
    {"id": 1, "username": "alice", "verified": True},
    {"id": 2, "username": "bob", "verified": False},
    {"id": 3, "username": "charlie", "verified": True},
]
verified_users = list(
    map(lambda u: u["username"].upper(), filter(lambda u: u["verified"], api_response))
)
print("Verified Users:", verified_users)
# ['ALICE', 'CHARLIE']



# 5. Sentiment Scoring (Map + Reduce in NLP)
print("\n--- Example 5: Sentiment Scoring ---")
words = ["good", "excellent", "bad", "good", "terrible"]
sentiment = {"good": 1, "excellent": 2, "bad": -1, "terrible": -2}
scores = list(map(lambda w: sentiment.get(w, 0), words))
print("Scores:", scores)  # [1, 2, -1, 1, -2]
total_score = reduce(lambda acc, s: acc + s, scores, 0)
print("Total Sentiment Score:", total_score)  # 1



# 6. E-Commerce Discounts (Map + Filter)
print("\n--- Example 6: E-Commerce Discounts ---")
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Phone", "price": 800},
    {"name": "Tablet", "price": 300},
    {"name": "Earbuds", "price": 50},
]
discounted = list(
    map(
        lambda p: {**p, "discounted_price": round(p["price"] * 0.9, 2)},
        filter(lambda p: p["price"] > 500, products),
    )
)
print("Discounted Products:", discounted)
# [{'name': 'Laptop', 'price': 1200, 'discounted_price': 1080.0}, {'name': 'Phone', 'price': 800, 'discounted_price': 720.0}]



# 7. IoT Sensor Data Processing
print("\n--- Example 7: IoT Sensor Data Processing ---")
sensor_readings = [22.5, 30.1, 35.2, 40.5, 19.0, 50.3]
abnormal = list(filter(lambda t: t > 40, sensor_readings))
print("Abnormal Readings:", abnormal)  # [40.5, 50.3]
fahrenheit = list(map(lambda c: round(c * 9 / 5 + 32, 1), sensor_readings))
print("In Fahrenheit:", fahrenheit)
# [72.5, 86.2, 95.4, 104.9, 66.2, 122.5]