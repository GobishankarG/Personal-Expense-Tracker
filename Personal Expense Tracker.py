import json
from datetime import datetime

expenses = []

def add_expense():
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., Food, Transport): ")
    date = input("Enter date (YYYY-MM-DD): ")

    expense = {
        "description": description,
        "amount": amount,
        "category": category,
        "date": date
    }
    expenses.append(expense)
    print("Expense added successfully.")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['description']} - ₹{expense['amount']} ({expense['category']}) on {expense['date']}")

def delete_expense():
    view_expenses()
    index = int(input("Enter the expense number to delete: ")) - 1
    if 0 <= index < len(expenses):
        deleted_expense = expenses.pop(index)
        print(f"Deleted: {deleted_expense['description']}")
    else:
        print("Invalid selection.")

def summarize_by_category():
    summary = {}
    for expense in expenses:
        category = expense['category']
        summary[category] = summary.get(category, 0) + expense['amount']
    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")

def calculate_total():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total expenses: ₹{total:.2f}")

def save_data():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)
    print("Data saved.")

def load_data():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        print("No saved data found.")

# Main Program
def main():
    load_data()
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Delete Expense\n4. Summarize by Category\n5. Calculate Total\n6. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            summarize_by_category()
        elif choice == '5':
            calculate_total()
        elif choice == '6':
            save_data()
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()