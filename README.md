# 💰 Python Express Tracker

A command-line expense tracking application built with Python.

This is my first independent Python project after completing a structured Python learning path. The purpose of this project was not to build a production-grade financial system, but to practice the transition from **learning Python concepts** to **designing, building, testing, debugging, and refactoring a working application independently**.

The project was intentionally developed through multiple versions. Each version improved the previous implementation rather than replacing it with a completely different system.

---

# 📌 Current Version

## V4 — Validation, Error Handling & Robustness

**V4 is the final planned version of Project 1 for now.**

The application now includes:

- Modular application structure
- JSON persistence
- Centralized loading and saving
- LOAD → MODIFY → SAVE data flow
- UUID-based expense IDs
- Date validation using `datetime`
- Expense-title validation
- Expense-amount validation
- Custom exceptions
- Empty-list handling
- Non-existent expense ID handling
- Delete-all confirmation
- JSON parsing error reporting
- More Pythonic iteration using direct iteration and `enumerate()`

The project is intentionally being frozen here so that the next learning stage can focus on a **new and more challenging Python application** instead of endlessly polishing the same CLI.

---

# ✨ Features

## 1. Add Expense

Users can add an expense by providing:

- Expense title
- Month
- Day
- Year
- Amount

Each expense receives a UUID-based identifier.

Example data:

```json
{
    "Id": "16aa1127-c1df-42b6-80fb-8e92eaba43fa",
    "Title": "Education",
    "Date": "2026-01-01",
    "Amount": 1500.0
}
```

---

## 2. View Expenses

The application loads the stored expense collection and displays the saved expenses.

---

## 3. Calculate Total Spending

The application loads the expense collection and calculates the total amount spent.

---

## 4. Delete an Expense

Users can enter an expense ID.

The application checks whether the ID exists before saving a deletion.

If the ID is not found, the application reports that the expense does not exist.

---

## 5. Delete All Expenses

The application requires the user to explicitly type:

```text
confirm
```

before removing all expenses.

If the list is already empty, the application reports that there are no expenses to delete.

---

# 🛠️ Technologies Used

- Python 3
- `json`
- `uuid`
- `datetime`
- File I/O
- Custom Python exceptions
- Git / GitHub

No database, web framework, AI framework, or third-party service is required.

---

# 📂 Project Structure

```text
expense_tracker_CLI_python/
│
├── expenses_details/
│   └── full_details.json
│
├── main.py
├── user_action_methods.py
├── custom_exceptions.py
└── README.md
```

## `main.py`

Acts as the CLI entry point.

Its primary responsibility is to:

- Display the menu
- Read the user's operation
- Delegate the selected operation to `user_action_methods.py`

The current menu uses Python's `match` statement.

## `user_action_methods.py`

Contains the application's expense operations and JSON persistence functions.

Important functions include:

```text
load_expenses()
save_expenses(expenses)
add_expense()
view_expenses_list()
get_total_spent_amount()
delete_expense_from_list()
delete_all_expenses()
```

## `custom_exceptions.py`

Contains custom exceptions used for specific validation failures:

```text
InvalidTextError
InvalidAmountError
```

## `expenses_details/full_details.json`

Stores the expense records as JSON.

---

# 🧩 Data Structure

The application stores expenses as a list of dictionaries.

Example:

```json
[
    {
        "Id": "16aa1127-c1df-42b6-80fb-8e92eaba43fa",
        "Title": "Education",
        "Date": "2026-01-01",
        "Amount": 1500.0
    },
    {
        "Id": "6463e0eb-e989-4585-a0e6-37e93a909337",
        "Title": "University registration",
        "Date": "2026-05-02",
        "Amount": 200.0
    }
]
```

---

# 🚀 Running the Application

## Prerequisites

Install Python 3.

Check the version:

```bash
python --version
```

## Run

From the project directory:

```bash
python main.py
```

---

# 🖥️ Application Menu

The application currently supports:

```text
1 - Add expense
2 - View all expenses
3 - View total spending
4 - Delete an expense
5 - Delete all expenses
q - Quit
```

---

# 🔄 Version History

## V1 — Initial Working Implementation

The first version focused on getting the application working.

Implemented:

- Add expense
- View expenses
- Calculate total
- Delete expense
- JSON persistence
- UUID generation
- Basic exception handling

Most functionality initially existed inside one large `while` loop in `main.py`.

### Main lesson

> **I can take a simple requirement and turn it into a functioning Python application.**

---

## V2 — Modular CLI Upgrade

V2 introduced the first significant structural improvement.

The expense operations were moved from `main.py` into:

```text
user_action_methods.py
```

Additional improvements included:

- Python `match` statement
- Date construction with `datetime.date()`
- Delete-all functionality
- Delete-all confirmation
- Better feedback when a requested expense ID does not exist

### Main lesson

> **A program can be split into modules with clearer responsibilities.**

---

## V3 — Storage Refactoring

V3 introduced two important persistence functions:

```text
load_expenses()
save_expenses(expenses)
```

The application moved toward a consistent data flow:

```text
LOAD
 ↓
MODIFY
 ↓
SAVE
```

Example:

```text
Add expense
    ↓
load_expenses()
    ↓
append new expense
    ↓
save_expenses(expenses)
```

The same pattern was applied to deletion and delete-all operations.

This reduced duplicated JSON access and removed the need for a shared module-level expense list.

### Main lesson

> **Storage responsibility and application responsibility should be separated.**

---

## V4 — Validation, Error Handling & Robustness

V4 focused on making the existing application harder to break.

### Input validation

The application now validates:

- Blank expense titles
- Numeric expense amounts
- Positive expense amounts
- Invalid dates through `datetime.date()`

### Custom exceptions

Two validation exceptions were introduced:

```text
InvalidTextError
InvalidAmountError
```

### Storage error handling

Malformed JSON is detected using `JSONDecodeError`.

The application reports:

- The parsing error message
- The line number
- The column number

The project intentionally does **not** attempt automatic repair of corrupted JSON.

This was an important design decision: corrupted storage should not automatically be rewritten without a deliberate recovery strategy.

### Empty-state handling

The application handles:

- No expenses available for deletion
- Non-existent expense IDs
- Delete-all confirmation

### Pythonic improvements

The project also moved toward:

- Direct iteration over collection items
- `enumerate()` when both index and item are genuinely required

### Main lesson

> **Software should distinguish valid input, invalid input, missing data, corrupted data, and normal empty states.**

---

# 🏗️ Current Architecture

The final project remains intentionally simple:

```text
                 ┌─────────────────┐
                 │     main.py     │
                 │   CLI / Menu    │
                 └────────┬────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ user_action_methods.py │
              │                        │
              │ Expense Operations     │
              │ + JSON Persistence     │
              └───────────┬────────────┘
                          │
                 ┌────────┴─────────┐
                 ▼                  ▼
        load_expenses()     save_expenses(expenses)
                 │                  │
                 └────────┬─────────┘
                          ▼
               ┌──────────────────────┐
               │   full_details.json  │
               │    Persistent Data   │
               └──────────────────────┘
```

This architecture is deliberately small.

There is no:

- Database
- REST API
- Authentication
- Frontend
- Docker
- Cloud deployment
- AI service
- FastAPI
- Flask

Those belong to later projects.

---

# 🧠 Important Engineering Pattern

One of the most important concepts learned during this project was:

```text
LOAD → MODIFY → SAVE
```

This separates the idea of:

```text
Reading persistent state
```

from:

```text
Changing application state
```

and:

```text
Writing persistent state
```

This simple pattern provides a foundation for understanding larger systems later.

---

# 🧪 Testing Approach

The application was tested manually through the CLI.

## Normal operations

- Add an expense
- View expenses
- Calculate total
- Delete an existing expense
- Delete a non-existent expense
- Delete all expenses
- Cancel delete-all
- Quit application

## Invalid input

- Blank title
- Whitespace-only title
- Non-numeric amount
- Zero amount
- Negative amount
- Invalid month
- Invalid day
- Invalid year
- Unknown expense ID

## Storage problems

- Missing JSON file
- Malformed JSON

The purpose of these tests was to intentionally exercise both normal and failure paths.

---

# ⚠️ Known Limitations

This project is **not production financial software**.

Some limitations remain intentionally.

## 1. JSON storage

JSON is sufficient for this learning project but would not be appropriate for a larger multi-user application.

## 2. No automated test suite

The project was primarily validated through manual CLI testing.

A future project can introduce automated testing in a more appropriate context.

## 3. No advanced schema validation

The project uses simple JSON persistence and does not implement a full data-validation framework.

## 4. Financial precision

Amounts are represented using Python `float`.

A production financial system would require more careful treatment of monetary precision.

## 5. No concurrency or transactional guarantees

This is a local single-user CLI application.

---

# 📊 V1 → V4 Progression

| Area | V1 | V2 | V3 | V4 |
|---|---|---|---|---|
| Working CLI | ✅ | ✅ | ✅ | ✅ |
| Modular structure | ❌ | ✅ | ✅ | ✅ |
| `match` menu | ❌ | ✅ | ✅ | ✅ |
| Date validation | ❌ | ✅ | ✅ | ✅ |
| Delete-all | ❌ | ✅ | ✅ | ✅ |
| Delete ID verification | ❌ | ✅ | ✅ | ✅ |
| Centralized loading | ❌ | ❌ | ✅ | ✅ |
| Centralized saving | ❌ | ❌ | ✅ | ✅ |
| LOAD → MODIFY → SAVE | ❌ | ❌ | ✅ | ✅ |
| Blank-title validation | ❌ | ❌ | ❌ | ✅ |
| Amount validation | ❌ | ❌ | ❌ | ✅ |
| Custom validation exceptions | ❌ | ❌ | ❌ | ✅ |
| JSON parse error reporting | ❌ | ❌ | ❌ | ✅ |
| Pythonic iteration | ❌ | Partial | Partial | ✅ |
| Edge-case handling | Basic | Improved | Improved | Stronger |

---

# 📈 Final Project Assessment

## Project 1 — Final V4 Assessment

| Category | Score |
|---|---:|
| Functionality | 9/10 |
| Python fundamentals | 8.5/10 |
| File handling | 8.5/10 |
| Error handling | 7.5/10 |
| Input validation | 8.5/10 |
| Code organization | 8.5/10 |
| Data modeling | 7.5/10 |
| Maintainability | 8/10 |
| Pythonic style | 8.5/10 |
| Independent problem solving | 9.5/10 |

### Overall learning-project score

# **8.5 / 10**

The most important result is not the number.

This project demonstrates a transition from:

> **“I know Python.”**

to:

> **“I can independently build and improve a Python application.”**

---

# 🧠 What I Learned

Through the four versions, I practiced:

- Python fundamentals
- Modules
- Functions
- Lists and dictionaries
- File I/O
- JSON
- UUIDs
- Datetime handling
- Exception handling
- Custom exceptions
- Input validation
- Data persistence
- State modification
- Refactoring
- Debugging
- Edge-case thinking
- Git branching
- Iterative software development

More importantly, I practiced a development cycle:

```text
Understand
    ↓
Design
    ↓
Code
    ↓
Test
    ↓
Debug
    ↓
Review
    ↓
Refactor
    ↓
Improve
```

---

# 🚀 Project-Based Python Progression

Python Express Tracker is the first project in a larger progression:

```text
Project 1
Expense Tracker CLI
        ↓
Project 2
Smart File Organizer
        ↓
Project 3
API Information CLI
        ↓
Project 4
URL Shortener API
        ↓
Project 5
AI Text Summarizer API
        ↓
Project 6
Cited PDF RAG Assistant
        ↓
Project 7
AI Interview Evaluator
        ↓
Project 8
Automated AI Evaluation Harness
        ↓
Project 9
Human-in-the-Loop AI Agent
        ↓
Project 10
Full-Stack AI Platform
```

---

# 🎯 Is Project 1 Finished?

**Yes.**

For the purpose of this learning progression, V4 should be considered the **final version of Project 1 for now**.

A V5 could certainly be created, but it is **not recommended at this stage**.

Adding categories, search, reports, CSV export, SQLite, classes, or other features would likely turn V5 into feature creep rather than meaningful progression for the current learning goal.

The recommended engineering decision is:

```text
Finish Project 1
      ↓
Commit V4
      ↓
Tag/version it
      ↓
Move to Project 2
```

Future robustness improvements can be revisited later if a later project makes them relevant.

---

# 🚀 Next Project

## Project 2 — Smart File Organizer

The next project will introduce a different class of Python problems:

```text
pathlib
   ↓
Directories
   ↓
File extensions
   ↓
File discovery
   ↓
File movement
   ↓
Duplicate names
   ↓
Safe operations
   ↓
Filesystem error handling
```

The project will continue using the same learning loop:

```text
Understand
→ Design
→ Code
→ Test
→ Debug
→ Review
→ Refactor
```

The architecture will be designed from requirements rather than given upfront.

---

# 👨‍💻 Author

**Abhishek**

Software Engineering & AI Engineering Learner

---

# ⭐ Final Note

Python Express Tracker is intentionally small.

Its purpose was to establish the engineering foundation needed for larger Python and AI systems.

The project represents the first step from:

**Learning Python → Building Python software.**

**Build → Test → Understand → Refactor → Improve → Build Something Harder. 🚀**
