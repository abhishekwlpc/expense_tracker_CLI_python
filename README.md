# 💰 Python Express Tracker

A command-line expense tracking application built with Python.

This is my first independent Python project created to move from learning Python syntax and concepts to building a working application. The project is being developed through multiple versions so that each version improves the previous implementation rather than replacing it with a completely different system.

## 📌 Current Version

**V3 — Storage Refactoring & Application Flow**

V3 focuses on separating JSON persistence from individual expense operations.

The project now uses:

- `load_expenses()` to read expense data
- `save_expenses(expenses)` to persist expense data
- A **LOAD → MODIFY → SAVE** pattern for operations that change data
- Local variables instead of a module-level shared `expense_list`

V3 intentionally does not introduce databases, web frameworks, classes, AI, or other advanced technologies.

## ✨ Features

- Add expenses
- View saved expenses
- Calculate total spending
- Delete an individual expense
- Delete all expenses with confirmation
- Persistent JSON storage
- UUID-based expense IDs
- Date creation using Python's `datetime`
- Separate CLI entry point and user-action module
- Centralized JSON loading and saving
- LOAD → MODIFY → SAVE application flow

## 🛠️ Technologies Used

- Python 3
- `json`
- `uuid`
- `datetime`
- File I/O
- Git / GitHub

No third-party Python packages are required.

## 📂 Project Structure

```text
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

Acts as the CLI entry point. It displays the menu and delegates operations to `user_action_methods.py`.

### `user_action_methods.py`

Contains the current implementations for loading and saving expenses, adding, viewing, calculating, and deleting expenses.

### `expenses_details/full_details.json`

Stores the expense records persistently as a JSON array.

## 🧩 Data Structure

Each expense is stored as a dictionary:

```json
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

```bash
python --version
```

### Run

```bash
python main.py
```

## 🖥️ Application Menu

```text
1 - Add expense
2 - View all expenses
3 - View total spending
4 - Delete an expense
5 - Delete all expenses
q - Quit
```

# 🔄 Version History

## V1 — Initial Working Implementation

Focused on making the application functional:

- Adding expenses
- Viewing expenses
- Calculating total spending
- Deleting expenses
- JSON persistence
- UUID-based IDs
- Basic exception handling

Most application logic was initially inside the main CLI loop.

## V2 — Modular CLI Upgrade

V2 introduced the first structural refactoring:

- Moved expense operations into `user_action_methods.py`
- Kept `main.py` focused on menu handling
- Used a `match` statement for menu selection
- Added delete-all expenses
- Added confirmation before deleting all expenses
- Improved date creation with `datetime.date()`
- Added detection for non-existent expense IDs

Architecture:

```text
main.py
   ↓
user_action_methods.py
   ↓
full_details.json
```

## V3 — Storage Refactoring

V3 focused on separating **application operations** from **JSON persistence**.

### New storage functions

```python
load_expenses()
save_expenses(expenses)
```

### `load_expenses()`

Responsible for reading the JSON file and returning the expense list.

```text
JSON file
    ↓
load_expenses()
    ↓
Python list
```

### `save_expenses(expenses)`

Responsible for writing the supplied expense list to the JSON file.

```text
Python list
    ↓
save_expenses(expenses)
    ↓
JSON file
```

### LOAD → MODIFY → SAVE

Operations that modify data now follow this general pattern:

```text
LOAD
 ↓
MODIFY
 ↓
SAVE
```

For example, adding an expense follows:

```text
load_expenses()
      ↓
append new expense
      ↓
save_expenses(expenses)
```

Deleting an expense follows the same pattern, and deleting all expenses loads the list, clears it, and saves the empty list.

## 🏗️ Current V3 Architecture

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
                │ Application Operations │
                │          +             │
                │ Storage Functions      │
                └───────────┬────────────┘
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
        load_expenses()       save_expenses(expenses)
                 │                     │
                 └──────────┬──────────┘
                            ▼
                 ┌──────────────────────┐
                 │   full_details.json  │
                 │    Persistent Data   │
                 └──────────────────────┘
```

V3 remains intentionally simple. There is still no database, FastAPI, Flask, authentication, AI, Docker, or cloud deployment.

## 📊 V2 → V3 Improvements

| Area | V2 | V3 |
|---|---|---|
| Module separation | ✅ | ✅ |
| JSON reading | Repeated in multiple functions | Centralized through `load_expenses()` |
| JSON writing | Repeated in multiple functions | Centralized through `save_expenses()` |
| Add operation | Mixed storage/application logic | LOAD → MODIFY → SAVE |
| Delete operation | Mixed storage/application logic | LOAD → MODIFY → SAVE |
| Delete-all operation | Direct JSON writing | LOAD → MODIFY → SAVE |
| Global expense list | Used previously | Removed from module-level design |
| Total calculation | Direct JSON access | Uses `load_expenses()` |
| View operation | Direct JSON access | Uses `load_expenses()` |

## ✅ What V3 Successfully Achieved

The main purpose of V3 was not to add features. It was to learn that a function should have a clear responsibility.

```text
load_expenses()
→ reads data

save_expenses(expenses)
→ writes data

add_expense()
→ creates and adds an expense

delete_expense()
→ removes an expense

calculate_total()
→ calculates a result
```

The project also introduced the important engineering pattern:

```text
LOAD → MODIFY → SAVE
```

## ⚠️ V3 Known Limitations

V3 is a **learning checkpoint**, not a production-quality implementation.

Remaining issues include:

- Exception handling is still too broad in places.
- Malformed JSON handling needs a more deliberate strategy.
- Some file/path handling can be improved.
- Input validation is incomplete.
- Some loops can be made more Pythonic.
- Some function names describe implementation details rather than intent.
- Expense amounts currently use `float`.

These are deliberately carried forward rather than hiding them with unnecessary complexity.

## 🧪 Current Testing

The project is currently tested manually through the CLI.

Important scenarios include:

### Valid input

- Add a normal expense
- Add multiple expenses
- View expenses
- Calculate total
- Delete an existing expense
- Delete all expenses after confirmation

### Invalid input

- Empty title
- Non-numeric amount
- Negative amount
- Zero amount
- Invalid date
- Invalid menu option
- Invalid expense ID

### File problems

- Missing JSON file
- Empty JSON file
- Malformed JSON
- Unexpected JSON structure
- File permission problems

# 🎯 V4 — Robustness, Validation & Error Handling

V4 will keep the same CLI + JSON architecture. No database, web framework, AI, or other advanced technology will be introduced yet.

### V4 goals

1. **Strong input validation**
   - Expense title
   - Amount
   - Date
   - Menu option
   - Expense ID
   - Confirmation input

2. **Better exception handling**
   - Use specific exceptions deliberately
   - Reduce broad `except Exception`
   - Separate user-input errors from storage errors

3. **Reliable JSON validation**
   - Distinguish missing data from corrupted data
   - Validate that loaded JSON has the expected structure

4. **Better empty-data behavior**
   - Graceful handling of an empty expense list
   - Useful output when there is nothing to display, calculate, or delete

5. **Cleaner CLI behavior**
   - Clearly reject unsupported menu choices
   - Preserve intentional quit behavior

6. **Remove unnecessary complexity**
   - Simplify index-based loops where indexes are not needed
   - Remove redundant conversions and handlers
   - Improve naming and readability

7. **Edge-case testing**
   - Deliberately test invalid user input and damaged storage states

## 🧠 V3 → V4 Learning Progression

```text
V1
Make it work
   ↓
V2
Separate the application into modules
   ↓
V3
Separate storage from application operations
   ↓
V4
Make the application robust
```

## 🚀 Project-Based Python Progression

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

## 📈 Current Project Status

| Item | Status |
|---|---|
| V1 initial implementation | ✅ Complete |
| V2 module separation | ✅ Complete |
| V3 storage refactoring | ✅ Complete checkpoint |
| Add expenses | ✅ Complete |
| View expenses | ✅ Complete |
| Calculate total | ✅ Complete |
| Delete expense | ✅ Complete |
| Delete-all confirmation | ✅ Complete |
| UUID IDs | ✅ Complete |
| JSON persistence | ✅ Complete |
| Centralized JSON loading | ✅ Complete |
| Centralized JSON saving | ✅ Complete |
| LOAD → MODIFY → SAVE | ✅ Complete |
| Robust exception strategy | 🔄 V4 |
| Strong input validation | 🔄 V4 |
| JSON structure validation | 🔄 V4 |
| Edge-case testing | 🔄 V4 |
| Automated tests | 🔄 Future |
| Database | 🔄 Future |
| Web API | 🔄 Future |

## 🧠 Development Philosophy

The development loop is:

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
    ↓
Build Something Harder
```

The goal is not simply to know Python. The goal is to become capable of independently designing, building, debugging, reviewing, and improving software.

## 👨‍💻 Author

**Abhishek**

Software Engineering & AI Engineering Learner

## ⭐ Final Note

Python Express Tracker is intentionally a small application.

Its real purpose is to build engineering habits before moving into larger Python, API, and AI systems.

**Build → Test → Understand → Refactor → Improve → Repeat. 🚀**
