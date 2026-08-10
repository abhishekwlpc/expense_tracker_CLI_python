# 💰 Python Express Tracker

A command-line expense tracking application built with Python.

Python Express Tracker is my first independent Python project created after completing my Python learning path. The purpose of this project was to move beyond simply learning Python syntax and concepts and start applying them to a real working application.

The application provides a simple command-line interface for adding, viewing, calculating, and deleting expenses while keeping the data persistent using a JSON file.

---

## 📌 Project Overview

Managing small personal expenses is a simple problem, but it provides a good opportunity to practice several fundamental software development concepts.

Python Express Tracker allows users to:

- Add expenses
- View saved expenses
- Calculate total spending
- Delete expenses
- Store data persistently in JSON
- Generate unique IDs for expenses
- Interact with the application through a CLI

The project intentionally uses a JSON file instead of a database because the primary goal of this version is to practice Python fundamentals, file handling, data structures, and application logic.

---

## 🎯 Project Goals

The main goals of this project were to practice:

- Python programming fundamentals
- Conditional statements
- Loops
- Lists and dictionaries
- User input handling
- File I/O
- JSON serialization and deserialization
- Exception handling
- Python modules
- UUID generation
- Basic application design
- Persistent application data
- Command-line application development

More importantly, the project was created to practice the transition from:

> **"I understand Python concepts."**

to:

> **"I can use Python to build a working application."**

---

# ✨ Features

## 1. ➕ Add Expense

Users can add a new expense by providing:

- Expense title
- Expense date
- Expense amount

Each expense receives a unique UUID.

Example:

```json
{
  "Id": "550e8400-e29b-41d4-a716-446655440000",
  "Title": "Education",
  "Date": "2026/06/03",
  "Amount": 1560.75
}
```

## 2. 📋 View All Expenses

Users can view all currently stored expenses.

The application reads the saved JSON data and displays the stored records through the command line.

---

## 3. 💵 Calculate Total Spending

The application calculates the total amount spent across all stored expenses.

Example:

```text
TOTAL AMOUNT SPEND SO FAR

Total Amount you spend so far is: 24927.75
```

---

## 4. 🗑️ Delete an Expense

Users can delete an expense by providing its unique ID.

Example:

```text
Please enter id of item that you want to delete:
550e8400-e29b-41d4-a716-446655440000
```

---

## 5. 💾 Persistent JSON Storage

Expenses are stored in:

```text
expenses_details/full_details.json
```

Because the data is stored in a file, expenses remain available even after the application is closed.

---

## 6. 🆔 UUID-Based Expense IDs

The application uses Python's built-in `uuid` module to generate unique identifiers:

```python
ide = str(uuid.uuid4())
```

This allows each expense to have its own identifier.

---

# 🛠️ Technologies Used

## Programming Language

- Python 3

## Python Modules

### `json`

Used for:

- Reading JSON data
- Writing JSON data
- Serializing Python objects
- Deserializing JSON data

Example:

```python
data = json.load(file)
```

and:

```python
json.dump(expense_list, file, indent=4)
```

---

### `uuid`

Used to generate unique identifiers for expenses.

Example:

```python
ide = str(uuid.uuid4())
```

---

# 📂 Project Structure

```text
expense_tracker_CLI_python/
│
├── expenses_details/
│   └── full_details.json
│
├── main.py
│
└── README.md
```

### `main.py`

Contains the main application logic and command-line interface.

### `expenses_details/full_details.json`

Stores the expense data.

### `README.md`

Contains project documentation.

---

# 📊 Data Structure

Each expense is represented as a Python dictionary.

Example:

```python
one_expense = {
    "Id": ide,
    "Title": title,
    "Date": date,
    "Amount": amount
}
```

The expenses are stored as a list of dictionaries.

Example:

```json
[
  {
    "Id": "550e8400-e29b-41d4-a716-446655440000",
    "Title": "Education",
    "Date": "2026/06/03",
    "Amount": 1560.75
  },
  {
    "Id": "8f14e45f-ea1b-4a6b-9c4e-123456789abc",
    "Title": "Shopping",
    "Date": "2026/06/03",
    "Amount": 23567.0
  }
]
```

---

# ▶️ Installation & Setup

## Prerequisites

Make sure Python is installed on your system.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

No external packages are required for the current version.

The project uses Python's standard library.

---

# 🚀 Running the Application

## 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

## 2. Navigate to the project

```bash
cd expense_tracker_CLI_python
```

## 3. Run the application

```bash
python main.py
```

---

# 🖥️ Application Menu

When the application starts, it displays the following options:

```text
Welcome to the Python Express Tracker!

-> To Add expense, type 1 and press enter
-> To See all expenses and total amount you send, type 2 and press enter
-> To See total spend amount, type 3 and press enter
-> To Delete an expense from the list, type 4 and press enter
-> To quit please enter q
```

---

# 🔄 Example Usage

## Add an Expense

Select:

```text
1
```

Then provide:

```text
Expense name/title: Education
Date: 2026/06/03
Amount: 1560.75
```

The application stores the expense in the JSON file.

Output:

```text
ADDED SUCCESSFULLY
```

---

## View Expenses

Select:

```text
2
```

The application loads the JSON file and displays the stored expenses.

---

## Calculate Total

Select:

```text
3
```

The application calculates the total amount of all stored expenses.

Example:

```text
Total Amount you spend so far is: 24927.75
```

---

## Delete Expense

Select:

```text
4
```

The application displays the existing expenses and asks for the ID of the expense to remove.

---

## Exit

Enter:

```text
q
```

or:

```text
quit
```

---

# 🧠 What I Learned

This project helped me practice several important Python concepts.

## Python Fundamentals

- Variables
- Strings
- Integers
- Floating-point numbers
- Conditional statements
- `while` loops
- `for` loops
- Lists
- Dictionaries
- User input
- Type conversion

---

## File Handling

I practiced:

- Opening files
- Reading files
- Writing files
- Using `with open(...)`
- JSON serialization
- JSON deserialization
- Persistent data storage

Example:

```python
with open("expenses_details/full_details.json", "r") as file:
    data = json.load(file)
```

---

## Working With Modules

The project uses Python's standard library modules:

```python
import json
import uuid
```

This helped me understand how external functionality can be incorporated into a Python application.

---

## Exception Handling

The application includes exception handling to prevent invalid user input from immediately terminating the application.

Example:

```python
try:
    ...
except ValueError:
    ...
```

---

## CLI Application Development

I learned how to build an interactive command-line application where users can:

1. Select an operation
2. Provide input
3. Process the input
4. Store or retrieve data
5. Continue using the application
6. Exit when finished

---

# 🧩 Application Flow

The current application follows a simple flow:

```text
                 ┌──────────────────┐
                 │ Start Application │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Display CLI Menu │
                 └────────┬─────────┘
                          │
          ┌───────────────┼────────────────┐
          │               │                │
          ▼               ▼                ▼
     Add Expense     View Expenses     Calculate Total
          │               │                │
          └───────────────┼────────────────┘
                          │
                          ▼
                   Delete Expense
                          │
                          ▼
                    Return to Menu
                          │
                          ▼
                         Quit
```

---

# 🏗️ Current Architecture

The current version intentionally uses a simple architecture:

```text
User
  │
  ▼
CLI
  │
  ▼
Python Application Logic
  │
  ▼
JSON File
```

There is currently no:

- Database
- Web API
- Authentication
- Frontend
- Cloud deployment

These are outside the scope of this first project.

---

# 🔍 Project Evaluation

## Version

**V2.0**

## Overall Assessment

| Area                        | Score |
| --------------------------- | ----: |
| Functionality               |  8/10 |
| Python Fundamentals         |  8/10 |
| File Handling               |  7/10 |
| Error Handling              |  6/10 |
| Input Validation            |  5/10 |
| Code Organization           |  5/10 |
| Data Modeling               |  7/10 |
| Maintainability             |  5/10 |
| Independent Problem Solving |  9/10 |

### Overall Project Score

# **7.5 / 10**

The most important result is not the numerical score.

The project successfully demonstrates that I can independently take a simple requirement and turn it into a functioning Python application.

---

# ✅ Current Strengths

The current version successfully implements:

- Working command-line interface
- Adding expenses
- Viewing expenses
- Calculating total spending
- Deleting expenses
- JSON persistence
- UUID-based IDs
- Basic exception handling
- User interaction
- Python standard library usage

---

# ⚠️ Current Limitations

This is an early-stage learning project, and several areas can be improved.

## 1. Application logic is concentrated in one loop

Most functionality currently exists inside one large `while` loop.

As the application grows, this will become difficult to maintain.

A future version should separate responsibilities into functions such as:

```python
load_expenses()
save_expenses()
add_expense()
view_expenses()
calculate_total()
delete_expense()
```

---

## 2. File operations are repeated

The JSON file is opened in multiple sections of the application.

A future version should centralize file loading and saving.

---

## 3. Input validation can be improved

The current application needs stronger validation for:

- Empty titles
- Invalid dates
- Invalid amounts
- Negative amounts
- Invalid expense IDs
- Invalid menu options

---

## 4. Error handling can be more specific

The current application uses a broad exception handler:

```python
except Exception as e:
```

Future versions should handle specific expected errors where appropriate.

Potential examples include:

```text
ValueError
FileNotFoundError
JSONDecodeError
PermissionError
```

---

## 5. Delete operation needs better feedback

The current implementation should distinguish between:

```text
Expense successfully deleted
```

and:

```text
Expense ID not found
```

This will be improved in a future version.

---

## 6. Date validation

The application currently accepts the date as a string.

For example:

```text
hello
```

could technically be entered as a date.

Future versions should validate the date format.

---

## 7. Financial precision

The current implementation uses Python `float` for expense amounts.

For a production financial application, a more appropriate representation such as `Decimal` could be considered.

This is intentionally outside the scope of the current beginner project.

---

# 🚀 Future Development Roadmap

## Version 3 — Refactoring

Planned improvements:

- [ ] Separate application logic into functions
- [ ] Create reusable `load_expenses()` function
- [ ] Create reusable `save_expenses()` function
- [ ] Improve input validation
- [ ] Improve exception handling
- [ ] Detect unsuccessful deletion
- [ ] Validate expense dates
- [ ] Improve CLI output
- [ ] Remove unnecessary loops

---

## Version 4 — Additional Features

Potential features:

- [ ] Expense categories
- [ ] Search expenses
- [ ] Update expenses
- [ ] Monthly spending reports
- [ ] Category-based spending reports
- [ ] Export expenses to CSV
- [ ] Better CLI formatting

---

## Future Architecture

As my Python skills improve, this simple project will be followed by progressively more advanced applications.

The learning progression will be:

```text
Python CLI
    ↓
File Handling
    ↓
External APIs
    ↓
FastAPI
    ↓
REST APIs
    ↓
Databases
    ↓
AI APIs
    ↓
RAG
    ↓
AI Evaluation
    ↓
AI Agents
    ↓
Production AI Systems
```

---

# 📚 Learning Journey

This project is part of a larger project-based Python learning approach.

Instead of continuing to watch beginner Python courses, the next stage focuses on building progressively more complex applications.

### Project progression

```text
Project 1
Expense Tracker
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

The difficulty will increase gradually rather than jumping directly from beginner Python into complex AI systems.

---

# 🎯 Why This Project Matters

Although this is a small application, it represents an important step in my learning journey.

There is a major difference between:

> **Watching someone build a project**

and:

> **Designing and building a project yourself.**

This project was created independently to practice that second skill.

The project is intentionally simple because the goal is to establish a foundation for larger systems.

---

# 📈 Engineering Skills Being Developed

Through this project and the projects that follow, I am working toward developing the ability to:

- Understand requirements
- Design simple solutions
- Choose appropriate data structures
- Work with files and APIs
- Handle errors
- Validate user input
- Debug problems
- Refactor code
- Write maintainable applications
- Test edge cases
- Document projects
- Use Git and GitHub
- Build increasingly complex systems

---

# 🧪 Testing

The current version has been manually tested through the command-line interface.

Basic scenarios include:

### Add

```text
Valid title
Valid date
Valid amount
```

### View

```text
Display stored expenses
```

### Calculate

```text
Calculate total of stored expenses
```

### Delete

```text
Provide an existing expense ID
```

### Exit

```text
q
quit
```

Future versions will introduce more systematic testing and edge-case coverage.

---

# 🔐 Security & Production Considerations

This project is intended for learning and is **not a production financial management system**.

The current version does not include:

- Authentication
- Authorization
- Encryption
- Database transactions
- Multi-user support
- Audit logging
- API security
- Cloud deployment

These concerns would need to be addressed before using a system like this in a real production environment.

---

# 💡 Possible Future Improvements

Some ideas for future development include:

### Storage

```text
JSON
 ↓
SQLite
 ↓
MySQL/PostgreSQL
```

### Interface

```text
CLI
 ↓
REST API
 ↓
Web Application
```

### Architecture

```text
Single Python File
        ↓
Modular Python Application
        ↓
FastAPI Backend
        ↓
Production Architecture
```

---

# 📊 Project Status

| Item                 | Status      |
| -------------------- | ----------- |
| Project concept      | ✅ Complete |
| CLI interface        | ✅ Complete |
| Add expenses         | ✅ Complete |
| View expenses        | ✅ Complete |
| Calculate total      | ✅ Complete |
| Delete expenses      | ✅ Complete |
| JSON persistence     | ✅ Complete |
| UUID IDs             | ✅ Complete |
| Basic error handling | ✅ Complete |
| Refactoring          | 🔄 Future   |
| Advanced validation  | 🔄 Future   |
| Categories           | 🔄 Future   |
| Reports              | 🔄 Future   |
| Database             | 🔄 Future   |
| Web API              | 🔄 Future   |

**Current Status: `Completed — V2.0`**

---

# 📝 Development Notes

This project is intentionally being developed through multiple versions.

The objective is not to write perfect code on the first attempt.

The development process is:

```text
Build
  ↓
Test
  ↓
Find problems
  ↓
Understand why
  ↓
Refactor
  ↓
Improve
  ↓
Build something harder
```

This approach will be continued throughout the rest of my Python and AI engineering projects.

---

# 👨‍💻 Author

**Abhishek**

Software Engineering & AI Engineering Learner

This project is part of my journey from software development toward AI engineering.

---

# ⭐ Final Note

This is my first independent Python project.

It is intentionally simple, but it represents an important milestone: moving from learning Python concepts to using Python to build software.

More complex projects will follow.

**Build → Learn → Improve → Repeat. 🚀**

````
