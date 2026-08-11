# 💰 Python Express Tracker

A command-line expense tracking application built with Python.

This is my first independent Python project created to move from
learning Python syntax and concepts to building a working application.
The project is being developed through multiple versions so that each
version improves the previous implementation rather than replacing it
with a completely different system.

## 📌 Current Version

**V2 --- Modular CLI Upgrade**

V2 introduces the first structural improvement over V1 by moving expense
operations out of `main.py` into a separate Python module.

## ✨ Features

-   Add expenses
-   View saved expenses
-   Calculate total spending
-   Delete an individual expense
-   Delete all expenses with confirmation
-   Persistent JSON storage
-   UUID-based expense IDs
-   Date creation and validation using Python's `datetime`
-   Separate CLI entry point and user-action module

## 🛠️ Technologies Used

-   Python 3
-   `json`
-   `uuid`
-   `datetime`
-   File I/O
-   Git / GitHub

No third-party Python packages are required.

## 📂 Project Structure

``` text
expense_tracker_CLI_python/
│
├── expenses_details/
│   └── full_details.json
│
├── main.py
├── user_action_methods.py
└── README.md
```

### `main.py`

Acts as the CLI entry point. It displays the menu and delegates
operations to `user_action_methods.py`.

### `user_action_methods.py`

Contains the current implementations for adding, viewing, calculating,
and deleting expenses.

### `expenses_details/full_details.json`

Stores the expense records persistently as a JSON array.

## 🧩 Data Structure

Each expense is stored as a dictionary:

``` json
{
    "Id": "16aa1127-c1df-42b6-80fb-8e92eaba43fa",
    "Title": "Education",
    "Date": "2026-01-01",
    "Amount": 1500.0
}
```

The JSON file contains a list of these expense objects.

## 🚀 Running the Application

### Prerequisites

Install Python 3.

Check the installed version:

``` bash
python --version
```

### Run

From the project directory:

``` bash
python main.py
```

## 🖥️ Application Menu

The application currently provides these operations:

``` text
1 - Add expense
2 - View all expenses
3 - View total spending
4 - Delete an expense
5 - Delete all expenses
q - Quit
```

## 🔄 V2 Implementation

### Add Expense

The user provides:

-   Expense title
-   Month
-   Day
-   Year
-   Amount

The application constructs a date using `datetime.date()` and generates
a UUID for the expense.

Example:

``` text
Expense title: Education
Month: 1
Date: 1
Year: 2026
Amount: 1500
```

### View Expenses

The application loads the JSON file and prints the stored expenses,
including:

-   ID
-   Title
-   Date
-   Amount

### Calculate Total

The application reads all expense records and calculates the total
amount spent.

### Delete Expense

The user provides an expense ID.

V2 now checks whether the entered ID actually exists and reports either:

``` text
DELETED SUCCESSFULLY
```

or:

``` text
Your Entered Item is not on the list
```

### Delete All Expenses

The application asks the user to type:

``` text
confirm
```

before removing all stored expenses.

## 🏗️ Current Architecture

V1 concentrated most application behavior inside the main `while` loop.

V2 introduces a basic separation:

``` text
                 ┌─────────────────┐
                 │     main.py     │
                 │   CLI / Menu    │
                 └────────┬────────┘
                          │
                          ▼
             ┌────────────────────────┐
             │ user_action_methods.py │
             │   Expense Operations   │
             └───────────┬────────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   full_details.json  │
              │    Persistent Data   │
              └──────────────────────┘
```

This is intentionally still a simple architecture. The project does not
yet use a database, classes, web APIs, or advanced frameworks.

## 📊 V1 → V2 Improvements

  --------------------------------------------------------------------------
  Area                    V1                      V2
  ----------------------- ----------------------- --------------------------
  CLI entry point         `main.py`               `main.py`

  Expense operations      Mostly inside main loop Moved to
                                                  `user_action_methods.py`

  Menu selection          Conditional logic       `match` statement

  Date handling           Free-form string        `datetime.date()`

  Delete feedback         Always reported success Checks whether ID exists

  Delete all              Not available           Added with confirmation

  Persistent storage      JSON                    JSON

  Expense IDs             UUID                    UUID
  --------------------------------------------------------------------------

## ⚠️ Known V2 Limitations

V2 is an improvement, but it is **not considered the final clean
implementation**.

The following issues remain intentionally available for the next
refactoring stage:

### 1. File I/O is still duplicated

Several functions directly open and parse:

``` text
expenses_details/full_details.json
```

This should eventually be centralized.

### 2. Global mutable state is used

`expense_list` exists as a module-level list.

This creates shared mutable state between functions and makes the
program harder to reason about.

### 3. Exception handling is inconsistent

Some functions catch broad `Exception`, while other functions allow
file-related errors to propagate.

V3 should distinguish expected errors such as:

-   `FileNotFoundError`
-   `json.JSONDecodeError`
-   `PermissionError`
-   `ValueError`

### 4. Input validation is incomplete

The application still needs stronger validation for:

-   Empty titles
-   Zero or negative amounts
-   Invalid numeric input
-   Invalid menu choices
-   Confirmation input
-   Expense ID format

### 5. JSON file assumptions

The application assumes that the JSON file already exists and contains
valid JSON.

V3 should handle missing and malformed files deliberately.

### 6. Some loops are unnecessary

Several operations iterate over lists using indexes such as:

``` python
for i in range(0, len(items)):
```

These can be simplified using direct iteration.

### 7. `delete_all_expenses()` uses an indirect deletion technique

The current implementation keeps only records whose ID equals:

``` text
not_a_id
```

This works for clearing the current data but is harder to understand
than directly representing the intention to clear the collection.

### 8. Financial precision

Expense amounts currently use `float`.

For a production financial application, `Decimal` would be worth
considering. It is intentionally not part of the current learning scope.

## 🎯 V3 Refactoring Goals

The next version will focus on **clean Python application structure**,
not new technologies.

Planned improvements:

-   [ ] Create `load_expenses()`
-   [ ] Create `save_expenses()`
-   [ ] Create `add_expense()`
-   [ ] Create `view_expenses()`
-   [ ] Create `calculate_total()`
-   [ ] Create `delete_expense()`
-   [ ] Handle missing JSON files
-   [ ] Handle malformed JSON
-   [ ] Use more specific exceptions
-   [ ] Validate expense titles
-   [ ] Validate expense amounts
-   [ ] Validate dates
-   [ ] Improve menu validation
-   [ ] Remove unnecessary loops
-   [ ] Reduce code duplication
-   [ ] Reduce or eliminate unnecessary global state
-   [ ] Improve readability and maintainability

V3 will remain a CLI application using JSON storage. No database,
FastAPI, Flask, AI, Docker, authentication, or other advanced
technologies will be introduced at this stage.

## 🧪 Testing Approach

The project is currently tested manually through the CLI.

Important V3 test cases will include:

### Valid input

-   Add a normal expense
-   View expenses
-   Calculate total
-   Delete an existing expense
-   Delete all expenses after confirmation

### Invalid input

-   Empty title
-   Non-numeric amount
-   Negative amount
-   Zero amount
-   Invalid month
-   Invalid day
-   Invalid year
-   Invalid menu option
-   Invalid expense ID

### File problems

-   Missing JSON file
-   Empty JSON file
-   Malformed JSON
-   Unexpected JSON structure
-   File permission problems

## 🧠 Engineering Lessons

This project is being used to practice more than Python syntax.

The main development loop is:

``` text
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

The objective is to develop the ability to independently turn
requirements into maintainable software.

## 🚀 Project-Based Python Progression

This project is the first step in a larger progression:

``` text
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

The difficulty will increase gradually, with each project building on
the engineering skills developed in previous projects.

## 📈 Current Status

  Item                           Status
  ------------------------------ -------------
  V1 initial implementation      ✅ Complete
  V2 module separation           ✅ Complete
  Add expenses                   ✅ Complete
  View expenses                  ✅ Complete
  Calculate total                ✅ Complete
  Delete expense                 ✅ Complete
  Delete-all confirmation        ✅ Complete
  UUID IDs                       ✅ Complete
  JSON persistence               ✅ Complete
  Date construction/validation   ✅ Partial
  Centralized file handling      🔄 V3
  Robust input validation        🔄 V3
  Specific exception handling    🔄 V3
  Reduced global state           🔄 V3
  Refactoring                    🔄 V3
  Automated tests                🔄 Future

## 👨‍💻 Author

**Abhishek**

Software Engineering & AI Engineering Learner

## ⭐ Final Note

Python Express Tracker is intentionally a small project.

The goal is not to make an expense tracker with every possible feature.
The goal is to repeatedly practice the engineering cycle of:

**Build → Test → Understand Problems → Refactor → Improve → Build
Something Harder**

This project will continue evolving through versions rather than being
replaced by a completely new implementation.
