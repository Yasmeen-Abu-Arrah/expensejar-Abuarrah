import csv
import random
from datetime import date, timedelta

def create_sample_data(filepath="expenses.csv"):
    categories = ["Food", "Transport", "Books", "Entertainment", "Health", "Other"]
    descriptions = {
        "Food":          ["Lunch", "Dinner", "Grocery", "Coffee", "Snack"],
        "Transport":     ["Bus ticket", "Taxi", "Fuel"],
        "Books":         ["Textbook", "Novel", "Notebook"],
        "Entertainment": ["Movie", "Game", "Concert", "Subscription"],
        "Health":        ["Pharmacy", "Doctor visit", "Vitamins"],
        "Other":         ["Gift", "Stationery", "Miscellaneous"],
    }

    today = date.today()
    rows  = [["date", "category", "amount", "description"]]

    for i in range(59, -1, -1):
        # Not every day has an expense — skip some days randomly
        # 0.3 --> 30% prob. to skip
        if random.random() < 0.3:
            continue
        day      = today - timedelta(days=i)
        category = random.choice(categories)
        amount   = round(random.uniform(2.0, 80.0), 2)
        desc     = random.choice(descriptions[category])
        rows.append([day.strftime("%Y-%m-%d"), category, amount, desc])

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Sample data saved: {filepath}  ({len(rows) - 1} expenses)")

if __name__ == "__main__":
    create_sample_data()