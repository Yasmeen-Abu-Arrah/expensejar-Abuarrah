from expense_manager import ExpenseManager
import matplotlib.pyplot as plt


class Visualizer():
    def category_pie(self, expenses: list):
        exp = ExpenseManager()
        totals = exp.total_by_category(expenses)

        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(
            totals.values(),
            labels=totals.keys(),
            autopct="%1.1f%%",
            startangle=140,
            wedgeprops={"edgecolor": "white", "linewidth": 1.5}
        )
        ax.set_title("Spending by Category", fontsize=14, fontweight="bold")
        plt.tight_layout()
        plt.show()

    def monthly_bar(self, expenses: list):
        exp = ExpenseManager()
        monthly = exp.monthly_totals(expenses)
        months = sorted(monthly.keys())

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(months, [monthly[m] for m in months], color="steelblue", edgecolor="black")
        ax.set_xlabel("Month")
        ax.set_ylabel("Total Spent (₪)")
        ax.set_title("Monthly Spending", fontsize=14, fontweight="bold")
        ax.set_xticklabels(months, rotation=30)

        for i, m in enumerate(months):
            ax.text(i, monthly[m] + 1, f"₪{monthly[m]}", ha="center", fontsize=10)
        plt.tight_layout()
        plt.show()
        