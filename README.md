# Expense Tracker

A simple command-line Expense Tracker built in Python. This project allows users to manage their daily expenses through a menu-based interface, with data stored locally in a JSON file so expenses are saved between sessions.

## Features

- Add new expenses
- View all saved expenses
- Calculate total money spent
- Search expenses by category
- Delete existing expenses
- Validate user input:
  - Date format checking
  - Category format checking
  - Amount validation
  - Menu/input error handling
- Save and load expenses using a JSON file

## How It Works

The program stores expenses as a list of dictionaries. Each expense contains:

- Date
- Category
- Amount

Example:

```python
{
    "Date": "14-07-2026",
    "Category": "Food",
    "Amount": 12.50
}
```

The data is saved in an `expenses.json` file using Python's built-in `json` module. When the program starts, previously saved expenses are loaded automatically.

## Technologies Used

- Python 3
- JSON file handling
- Built-in Python modules:
  - `datetime`
  - `json`

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/expense-tracker.git
```

2. Navigate to the project folder:

```bash
cd expense-tracker
```

3. Run the program:

```bash
python expense_tracker.py
```

## Usage

When the program starts, choose an option from the menu:

```
1. Add Expense
2. View All Expenses
3. View Total Spent
4. Search Expense
5. Delete Expense
6. Exit Expense Tracker
```

Follow the prompts to manage your expenses.

## Example Output

```
Actions Menu:
1. Add Expense
2. View All Expenses
3. View Total Spent
4. Search Expense
5. Delete Expense
6. Exit Expense Tracker

Choose the action you want to make: 1

Date: 14-07-2026
Category: Food
Amount: 12.5

Expense saved successfully!
```

## Future Improvements

Possible improvements for future versions:

- Add an edit expense feature
- Add graphical user interface (GUI)
- Add charts and spending statistics
- Use a database instead of JSON storage
- Add user accounts and multiple expense profiles

## Author

Created as a Python programming project to practice:

- Functions
- Loops
- Lists and dictionaries
- File handling
- Data validation
- JSON storage
