from expense_manager import ExpenseManager
from visualizer import Visualizer

def main():
    DATA_FILE = "expenses.csv"

    em  = ExpenseManager()
    viz = Visualizer()

    # Step 1: Load expenses
    print("[1/4] Loading expenses...")
    expenses = em.load(DATA_FILE)
    print(f"      Records loaded: {len(expenses)}\n")

    # Step 2: Add a new expense
    print("[2/4] Adding a new expense...")
    from datetime import date
    today = date.today().strftime("%Y-%m-%d")
    try:
        expenses = em.add_expense(expenses, today, "Food", 18.50, "University cafeteria")
        em.save(expenses, DATA_FILE)
        print(f"      Expense added for {today}")
    except ValueError as e:
        print(f"      Skipped: {e}")

    # Step 3: Show summary
    print("\n[3/4] Summary:")
    totals = em.total_by_category(expenses)
    grand_total = sum(totals.values())

    print(f"\n  {'Category':<15} {'Total (₪)':>12}  {'Share':>7}")
    print(f"  {'-'*15} {'-'*12}  {'-'*7}")
    for cat, total in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        share = round(total / grand_total * 100, 1)
        print(f"  {cat:<15} {total:>11.2f}₪  {share:>6}%")
    print(f"\n  Grand total: ₪{grand_total:.2f}")

    highest = em.find_highest(expenses)
    print(f"\n  Highest expense: ₪{highest['amount']} — {highest['description']} ({highest['date']})")

    # Step 4: Visualize
    print("\n[4/4] Displaying charts...")
    viz.category_pie(expenses)
    viz.monthly_bar(expenses)

    print("\nDone!")

if __name__ == "__main__":
    main()