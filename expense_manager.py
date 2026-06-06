import csv

VALID_CATEGORIES = ["Food", "Transport", "Books", "Entertainment", "Health", "Other"]

class ExpenseManager():
    def load(self, filepath: str) -> list:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                read = csv.DictReader(f)
                content = [r for r in read]
                return content 
        except FileNotFoundError: return []
    
    def save(self, expenses: list, filepath: str) -> None:
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            field_names = ["date", "category", "amount", "description"]
            write = csv.DictWriter(f, fieldnames=field_names)
            write.writeheader()
            write.writerows(expenses)
        print(f"Successfully saved :)")

    def add_expense(self, expenses: list, date_str: str, category: str, amount: float, description: str) -> list:
        if category not in VALID_CATEGORIES:
            raise ValueError(f"Category must be one of {VALID_CATEGORIES}")
        
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        
        expenses.append({
            "date":        date_str,
            "category":    category,
            "amount":      str(round(amount, 2)),
            "description": description
        })
        return expenses
    
    def total_by_category(self, expenses: list) -> dict:
        totals = {}
        for exp in expenses:
            cat = exp["category"]
            totals[cat] = round(totals.get(cat, 0) + float(exp["amount"]), 2)
        return totals
    
    def monthly_totals(self, expenses: list) -> dict:
        totals = {}
        for exp in expenses:
            month = exp["date"][:7]   # "YYYY-MM"
            totals[month] = round(totals.get(month, 0) + float(exp["amount"]), 2)
        return totals
    
    def find_highest(self, expenses: list) -> dict:
        if not expenses:
            return None
        return max(expenses, key=lambda e: float(e["amount"]))
    

    # Additional
    def check_budget(self, expenses: list, budget: dict) -> list:
        warn = []
        totals = self.total_by_category(expenses)
        for cat, limit in budget.items():
            spent = totals.get(cat,0)
            if spent > limit:
                warn.append(f"Warning! {cat}: spent {spent:.2f} of {limit:.2f} limit")
            else:
                remain = round(limit - spent, 2)
                warn.append(f"OK {cat}: spent {spent:.2f} of {limit:.2f} {remain:.2f} remaining :) ")
        return warn
    
    def search(self, expenses: list, keyword: str) -> list:
        if not keyword:
            raise ValueError("Its empty :)")
        keyword_l = keyword.lower()
        results = [exp for exp in expenses if keyword_l in exp["description"].lower()]
        return results

