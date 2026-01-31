# TODO решите задачу
import json
def task() -> float:
    data = [
        {"score": 0.0009456152645028281, "weight": 1},
        {"score": 0.5, "weight": 2},
        {"score": 0.2, "weight": 0.4},
        {"score": 0.3, "weight": 3.7},
        {"score": 0.105, "weight": 1},
    ]
    total = sum(item["score"] * item["weight"] for item in data)
    return round(total, 3)
print(task())

