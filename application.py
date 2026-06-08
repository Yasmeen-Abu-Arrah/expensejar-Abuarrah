from flask import Flask, jsonify, request, send_file
from expense_manager import ExpenseManager
import matplotlib 
matplotlib.use("AGG") #non - interactive back
import matplotlib.pyplot as plt
import io


app = Flask(__name__)
em = ExpenseManager()


DATA_FILE = "expenses.csv"
DEFAULT_BUDGETS = {
    "Food": 200,
    "Transport": 100,
    "Entertainment": 80,
    "Books": 150,
    "Health": 120,
    "Other": 60,
}
VALID_CATEGORIES = ["Food", "Transport", "Books", "Entertainment", "Health", "Other"]


@app.route("/expenses", methods=["GET"])
def get_expenses():
    expenses = em.load(DATA_FILE)
    return jsonify(expenses)


@app.route("/expenses/by-category", methods=["GET"])
def by_category():
    expenses = em.load(DATA_FILE)
    return jsonify(em.total_by_category(expenses))


@app.route("/expenses/category/<name>", methods=["GET"])
def by_category_fillter(name):
    if name not in VALID_CATEGORIES:
        return jsonify({"error": f"Sorry, unknown category: {name} :)"}), 400
    expenses = em.load(DATA_FILE)
    filtered = [exp for exp in expenses if exp["category"] == name]
    return jsonify({"category": name, "count": len(filtered), "expenses": filtered})


@app.route("/expenses/by-month", methods=["GET"])
def by_month():
    expenses = em.load(DATA_FILE)
    return jsonify(em.monthly_totals(expenses))


@app.route("/expenses/month/<month>", methods=["GET"])
def by_month_fillter(month):
    expenses = em.load(DATA_FILE)
    filtered = [exp for exp in expenses if exp["month"] == month]
    if not filtered:
        return jsonify({"error": f"No expenses found for {month} :)"}), 404
    total = round(sum(float(e["amount"]) for e in filtered),2)
    return jsonify({"month": month, "count": len(filtered), "total": total, "expenses": filtered})


@app.route("/expenses/highest", methods=["GET"])
def highest():
    expenses = em.load(DATA_FILE)
    result = em.find_highest(expenses)
    if result is None: 
        return jsonify({"messege": "Ni expenses found :)"}), 404
    return jsonify(result)


@app.route("/expenses/search", methods=["GET"])
def search():
    keyword = request.args.get("keyword","")
    try:
        expenses = em.load(DATA_FILE)
        results = em.search(expenses, keyword)
        return jsonify({"count": len(results), "results": results})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    

@app.route("/expenses/budget", methods=["GET"])
def budget():
    expenses = em.load(DATA_FILE)
    warn = em.check_budget(expenses, DEFAULT_BUDGETS)
    return jsonify(warn)


@app.route("/expenses/predict", methods=["GET"])
def predict():
    expenses = em.load(DATA_FILE)
    return jsonify(em.predict_month(expenses))



@app.route("/expenses", methods=["POST"])
def add_expenses():
    data = request.get_json()
    try:
        expenses = em.load(DATA_FILE)
        expenses = em.add_expense(expenses, data["date"], data["category"], float(data["amount"]), data["description"])
        em.save(expenses, DATA_FILE)
        return jsonify({"messege": "Expense Added successfully :)"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/expenses/<int:index>", methods= ["DELETE"])
def delete_expense(index):
    expenses = em.load(DATA_FILE)
    try:
        removed = expenses[index]
        expenses.pop(index)
        em.save(expenses, DATA_FILE)
        return jsonify({"messege": "Deletes successfully", "deleted": removed})
    except IndexError:
        return jsonify({"error": f"Index {index} not found here :)"}), 404


@app.route("/expenses/summary", methods= ["Get"])
def summery():
    expenses = em.load(DATA_FILE)
    total_by_cat = em.total_by_category(expenses)
    totals = round(sum(total_by_cat.values()),2)
    return jsonify({
        "total_records": len(expenses),
        "by_category": total_by_cat,
        "grand_total": totals,
        "by_month": em.monthly_totals(expenses),
        "highest_expense": em.find_highest(expenses),
        "prediction": em.predict_month(expenses)
    })


# Hi Mr.Hussen, in this part: 
# I used the code in the visualizer file :)
@app.route("/expenses/chart/pie", methods= ["Get"])
def chart_pie():
    expenses = em.load(DATA_FILE)
    totals = em.total_by_category(expenses)

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

    img = io.BytesIO()
    plt.savefig(img, format="png", bbox_inches="tight")
    plt.close()
    img.seek(0)
    return send_file(img, mimetype="image/png")


@app.route("/expenses/chart/bar", methods= ["Get"])
def chart_bar():
    expenses = em.load(DATA_FILE)
    monthly = em.monthly_totals(expenses)
    months = sorted(monthly.keys())

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(months, [monthly[m] for m in months], color="steelblue", edgecolor="black")
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Spent (₪)")
    ax.set_title("Monthly Spending", fontsize=14, fontweight="bold")
    ax.set_xticks(range(len(months))) #To prevent warning
    ax.set_xticklabels(months, rotation=30)

    for i, m in enumerate(months):
            ax.text(i, monthly[m] + 1, f"₪{monthly[m]}", ha="center", fontsize=10)
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format="png", bbox_inches="tight")
    plt.close()
    img.seek(0)
    return send_file(img, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True,port=3000)