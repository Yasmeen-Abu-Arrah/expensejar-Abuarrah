# ExpenseJar — Personal Expense Tracker
**Course:** Python Programming 

## 1. Project Title & Member
**project:** ExpenseJar — Personal Expense Tracker  
**Student:** Yasmeen Ahmad Abu Arrah - 202211471  
**Email:** y.abuarra1@gmail.com  
**GitHub Repo:** https://github.com/Yasmeen-Abu-Arrah/expensejar-Abuarrah.git 


## 2. Project Overview
The ExpenseJar is a Python-based application that enables users to keep track of their daily expenses. This application is capable of reading and writing data (date, category, amount, and description) from a CSV file in order to maintain data persistence even when not using the application.  
Additionally, it enables the addition of an expense transaction provided with data validation, calculating monthly expenditure in each category and determining which expense was the most costly. In order to make it easier for the user to interpret the results generated, ExpenseJar provides visualization of data using a pie chart and a bar graph, both created by Matplotlib library.   
Other functionalities include checking whether a certain category has reached its budget limit, searching the records using a keyword in description, and forecasting the monthly expenditure of the user based on his/her spending habits.

## 3. Libraries Used
| Library | Version | How it was used |
|---|---|---|
| csv | built-in | Loading and saving expense records |
| contourpy | 1.3.3 | Calculating and contouring cross-sections and of data (visualization) |
| cycler | 0.12.1 | Manage customizable cycles of colors and styles in plots |
| fonttools | 4.63.0 | Manipulation and conversion of font formats for text rendering |
| kiwisolver | 1.5.0 | Efficient layout resolution for plots and widgets |
| matplotlib | 3.10.9 | Pie and bar charts for categories and monthly totals |
| numpy | 2.4.6 | Numerical operations and efficient multi-dimensional array manipulation |
| packaging | 26.2 | Utilities for finding information about Python packages |
| pillow | 12.2.0 | Loading, processing, saving and working with image file formats |
| pyparsing | 3.3.2 | Parsing texts and mathematical expression handling inside charts |
| python-dateutil | 2.9.0.post0 | Additional features for date and time calculations in time-series axes |
| six | 1.17.0 | Utilities supporting Python runtime environments |


## 4. Modules Description
### expense_manager.py
Contains the ExpenseManager class. Its the core of the idea and the application. Use CSV file to handles all operation of data like, loading, saving, adding after validation, and computing the final statistics.  
total_by_category() and monthlu_totals() are the most important methods in this file. They are use dict.get(key,0) pattern to accumlate spending total.  
In addition, find the highest amount, check the budget by category, search using keyword, and pretict the total cost at the end of the month.  

### visualizer.py
Contains the Visualizer class. It takes the loaded data (expenses list) to produce Matplotib charts. The first is a pie chart, that show distributed spending across categories by the category_pie() method. The second is a bar chart, that show the total spending per month by monthly_bar() method.

### main.py
The main code to work. Actully, its the entry point of the application. It runs all steps: loading the CSV, adding a new expense, printing a summery, and displaying charts. All steps work as pipeline.

### create_sample_data.py
Its a script that no class required. Its gendreate a realistic expenses.csv file with random data spread over the last 60 days. It should be run once befor the main.py file


## 5. Test Cases
### Test 1: add_expense() — invalid category
**Input:** category = "Clothes" (not in VALID_CATEGORIES)
**Expected Output:** ValueError raised
**Actual Output:** ValueError: Category must be one of [...] ✅

**Code snippet used to verify:**
```python
from expense_manager import ExpenseManager
em = ExpenseManager()
try:
    em.add_expense([], "2026-05-10", "Clothes", 50.0, "New shirt")
    print("No error raised — FAIL")
except ValueError as e:
    print(f"Caught: {e} — PASS")
```

### Test 2: add_expense() — invalid category
**Input:** amount = 0
**Expected Output:** ValueError raised
**Actual Output:** ValueError: Amount must be greater than 0 ✅

**Code snippet used to verify:**
```python
from expense_manager import ExpenseManager
em = ExpenseManager()
try:
    em.add_expense([], "2026-05-10", "Food", 0, "Free lunch")
    print("No error raised — FAIL")
except ValueError as e:
    print(f"Caught: {e} — PASS")
```

### Test 3: total_by_category() — verify totals match manual sum
**Input:** a small list with 3 known Food entries (10, 20, 30 ₪)  
**Expected Output:** {"Food": 60.0} 
**Actual Output:** {"Food": 60.0} ✅

**Code snippet used to verify:**
```python
from expense_manager import ExpenseManager
em = ExpenseManager()
sample = [
    {"date": "2026-05-01", "category": "Food", "amount": "10.0", "description": "Lunch"},
    {"date": "2026-05-02", "category": "Food", "amount": "20.0", "description": "Dinner"},
    {"date": "2026-05-03", "category": "Food", "amount": "30.0", "description": "Grocery"},
]
result = em.total_by_category(sample)
print(result)   # Expected: {'Food': 60.0}
assert result["Food"] == 60.0, "FAIL"
print("PASS")
```


### Test 4: `find_highest()` — confirm it returns the correct record
**Input:** a list where the highest amount is 75.5 (Books)  
**Expected Output:** the dict with amount `"75.5"`  
**Actual Output:** correct record returned ✅

**Code snippet used to verify:**
```python
from expense_manager import ExpenseManager
em = ExpenseManager()
sample = [
    {"date": "2026-05-01", "category": "Food",  "amount": "15.0",  "description": "Lunch"},
    {"date": "2026-05-02", "category": "Books", "amount": "75.5",  "description": "Textbook"},
    {"date": "2026-05-03", "category": "Other", "amount": "8.0",   "description": "Gift"},
]
result = em.find_highest(sample)
print(result)   # Expected: the Books row
assert float(result["amount"]) == 75.5, "FAIL"
print("PASS")
```


### Test 5: main.py run — no errors, both charts appear
**Input:** run python create_sample_data.py then python main.py 
**Expected Output:** terminal prints all 4 steps, pie chart appears, then bar chart appears  
**Actual Output:** ran successfully with no errors ✅


### Test 6: check_budget() — category exceeded the limit
**Input:** Food budget = 50₪, actual spending = 108.50₪  
**Expected Output:** string contains "WARNING" and "Food"  
**Actual Output:** WARNING  Food: spent 108.50 of 50.00 limit ✅

**Code snippet used to verify:**
```python
from expense_manager import ExpenseManager
em = ExpenseManager()
sample = [
    {"date": "2026-06-06", "category": "Food", "amount": "18.50", "description": "Cafeteria"},
    {"date": "2026-06-03", "category": "Food", "amount": "90.00", "description": "Grocery"},
]
try:
    warn = em.check_budget(sample, {"Food": 50})
    has_warn = any("Warning!" in w and "Food" in w for w in warn)
    if not has_warn:
        print(f"No warning found - FAIL")
    else: print ("PASS")
except Exception as e:
    print(f"Unexpected error: {e} — FAIL")
```


### Test 7: search() — case-insensitive keyword match
**Input:** keyword = "LUNCH", description in data = "Cafeteria lunch"  
**Expected Output:** 1 result returned  
**Actual Output:** 1 result found ✅

**Code snippet used to verify:**
```python
from expense_manager import ExpenseManager
em = ExpenseManager()
sample = [
    {"date": "2026-06-06", "category": "Food",      "amount": "18.50", "description": "Cafeteria lunch"},
    {"date": "2026-06-05", "category": "Transport",  "amount": "5.00",  "description": "Bus ticket"},
]
try:
    results = em.search(sample, "LUNCH")
    if len(results) != 1:
        print(f"Expected 1 result, got {len(results)} — FAIL")
    elif results[0]["description"] != "Cafeteria lunch":
        print("Wrong record returned — FAIL")
    else:
        print("PASS")
except Exception as e:
    print(f"Unexpected error: {e} — FAIL")
```


## 6. Screenshots
### Category Pie Chart
![Pie](screenshots/category_pie.png)
*Pie chart showing spending distribution across categories*

### Monthly Bar Chart
![Bar](screenshots/monthly_bar.png)
*Bar chart showing total spending per month*

### Terminal Output
![Terminal](screenshots/terminal_output.png)
*Full output of running python main.py*


## 7. Invidual Contributions
| Student | ID | Files | Commit Count | GitHub Username |
|---|---|---|---|---|
| Yasmeen Ahmad Rafeeq Abuarrah | 202211471 | All files | 13 | Yasmeen-Abu-Arrah |


## 8. Challenges & What You Learned
**Challenge - My Virtual Environment Stopped Working After I Renamed the Folder**
When I renamed my project folder to include my name. My pip stopped working. I could not use "pip freeze". I found out that the virtual environment remembers the folder path. So when I renamed the folder it broke the environment. To fix this I got rid of the ".venv" and made a new one in the renamed folder. Then I installed matplotlib again before I made "requirements.txt".

**What I Learned**
I learned about reading and writing CSV files. I also learned about using "dict.get(key, 0)" to add up totals without having to check if something exists. I learned how to make charts with matplotlib and how to make "requirements.txt" using "pip freeze". The project was a learning experience, for me and I got to learn about these new things, like matplotlib and "pip freeze" and how to use them.


## 9. How to Run
### Install dependencies
```bash
pip install -r requirements.txt
```
> Generated with `pip freeze > requirements.txt`

### Create sample data
```bash
```python create_sample_data.py
```

### Run the app
```bash
python main.py
```