from flask import Flask, jsonify, request
from expense_manager import ExpenseManager

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


@app.route("/expenses", methods=["GET"])
def get_expenses():
    expenses = em.load(DATA_FILE)
    return jsonify(expenses)


@app.route("/expenses/by-category", methods=["GET"])
def by_category():
    expenses = em.load(DATA_FILE)
    return jsonify(em.total_by_category(expenses))


@app.route("/expenses/by-month", methods=["GET"])
def month():
    expenses = em.load(DATA_FILE)
    return jsonify(em.monthly_totals(expenses))


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


if __name__ == "__main__":
    app.run(debug=True,port=3000)