<h1 align="center">💰 ExpenseJar — Personal Expense Tracker</h1>
<br>

<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=3000&color=1D9E75&width=900&lines=ExpenseJar+💰+Personal+Expense+Tracker;Track+%7C+Analyze+%7C+Visualize+Your+Spending+📊;Built+with+Python+%2B+OOP+%2B+Matplotlib+🐍;By+Yasmeen+Ahmad+Rafeeq+Abuarra+·+✨">
  </a>
</p>

> <p align="left">
  <a href="#"><img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white"></a>
  <a href="#"><img src="https://img.shields.io/badge/matplotlib-3.10.9-orange?style=for-the-badge&logo=python&logoColor=white"></a>
  <a href="#"><img src="https://img.shields.io/badge/Data-CSV-green?style=for-the-badge&logo=files&logoColor=white"></a>
</p>


> **ExpenseJar** is a smart and lightweight Python-based application designed to help users store, analyze, validate, and visualize their daily financial expenses with interactive data pipelines.

---

## 👩‍💻 Student Profile

| Field | Details |
| :--- | :--- |
| 👤 **Name** | Yasmeen Ahmad Abuarra |
| 🆔 **Student ID** | 202211471 |
| 📧 **Email** | y.abuarra@student.aaup.edu |
| 📚 **Course** | Python Programming — Application Chapter |
| 👤 **Instrutor** | Mr. Hussein Younis |

---
## 📦 Core Features (What It Does)


```
expenses.csv  →  ExpenseManager  →  Visualizer
                  ├─ load()           ├─ category_pie()
                  ├─ save()           └─ monthly_bar()
                  ├─ add_expense()
                  ├─ total_by_category()
                  ├─ monthly_totals()
                  ├─ find_highest()
                  ├─ check_budget()
                  ├─ search()
                  └─ predict_month()
```

ExpenseJar goes beyond standard logging to provide a complete lifecycle for personal money management:

* **💾 Smart Persistence:** Reads and writes transaction records directly from/to a local `CSV` database file to ensure data is never lost.
* **🛡️ Robust Data Validation:** Prevents bad input entries (e.g., negative values, zero amounts, or unsupported categories) by raising explicit `ValueError` blocks immediately.
* **🔍 Flexible Search Engine:** Allows quick querying of past records using case-insensitive keyword matches across transaction descriptions.
* **⚠️ Budget Alert System:** Built-in automated monitoring that flags a `WARNING` message on the dashboard if spending in any category exceeds its defined budget threshold.
* **🔮 Predictive Analysis (`Predict`):** Implements a lightweight linear estimation algorithm that forecasts total end-of-month spending habits based on current velocity.
* **📊 Visual Analytics Dashboard:** Converts numerical rows into clear, production-ready visual representations (Pie charts for categorical weight and Bar charts for monthly comparison) using `Matplotlib`.

---

## 📁 Project Structure

```
ExpenseJar_Abuarra/
├── expense_manager.py      ← Core class: load, save, add, stats
├── visualizer.py           ← Charts: pie + bar
├── main.py                 ← Full pipeline
├── create_sample_data.py   ← Generates sample expenses.csv
├── expenses.csv            ← Expense records
├── requirements.txt        ← pip freeze output
├── report.md               ← Full project report
└── screenshots/
    ├── category_pie.png
    ├── monthly_bar.png
    └── terminal_output.png
```

---

## 🚀 How to Run

### 1️⃣ Clone the repo
```bash
git clone https://github.com/Yasmeen-Abu-Arrah/expensejar-Abuarrah.git
cd expensejar-Abuarrah
```

### 2️⃣ Create a virtual environment (recommended)
```bash
python -m venv .venv
```
Activate it:
- **Windows:** `.venv\Scripts\activate`
- **macOS / Linux:** `source .venv/bin/activate`

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Generate sample data & run the app
```bash
python create_sample_data.py
python main.py

```

---
<h3 align="center"> 💡 Feedback on code quality, logic, or new feature ideas is always welcome — feel free to reach out! We would greatly appreciate it. </h3>

