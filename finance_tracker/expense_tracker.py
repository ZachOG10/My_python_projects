"""
THIS IS MY FIRST PROJECT SINCE I LEANT PYTHON.
AN EXPENSE TRACKER 
This program keeps track of your income and expenses.
It helps you know exactly where your money goes.
"""
import json
from datetime import datetime

def save_transactions():
    with open("transactions.json", "w") as f:
        json.dump(transactions, f)

def load_transactions():
    try:
        with open("transactions.json", "r") as f:
            return json.load(f) 
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return [] 
def get_valid_amount(prompt_text):
    while True:
        try:
            value = float(input(prompt_text)) 
            if value <= 0:
                print("Amount must be positive. Try again.") 
                continue
            return value
        except ValueError:
            print("That's not a valid number. Please try again.")
def get_valid_description(decscription):
    while True:
        description = input("Enter a valid description use alphabets: ").strip()
        if description == "":
            print("Description cannot be empty. Try again.")
            continue
        return description
def add_transaction(transaction_type):
    transaction_amount = get_valid_amount("Enter amount: ")
    description = get_valid_description("Enter category/description: ") 
    ##Store the  current transaction as [type, amount, description]
    today = datetime.now().strftime("%Y-%m-%d")
    transaction = [transaction_type, transaction_amount, description, today]
    transactions.append(transaction)
    save_transactions() 
    print(f"{transaction_type.capitalize()} of {transaction_amount} added.")

def view_balance():
    total_income = 0.0
    total_expense = 0.0

    for transaction in transactions:
        if transaction[0] == "income":
            total_income += transaction[1]
        elif transaction[0] == "expense":
            total_expense += transaction[1]

    balance = total_income - total_expense

    print("\n--- FINANCIAL SUMMARY ---")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expense}")
    print(f"Balance: {balance}")

    if balance > 0:
        print("Your balance is positive.")
    elif balance == 0:
        print("You have broken even.")
    else:
        print("Your balance is negative.")

def view_all_transactions():
    if not transactions:
        print("No transactions recorded yet.")
    else:
        print("\n--- ALL TRANSACTIONS ---")
        for index, transaction in enumerate(transactions, start=1):
            transaction_type = transaction[0]
            transaction_amount = transaction[1]
            transaction_description = transaction[2]
            transaction_date = transaction[3] 
            print(f"{index}. {transaction_type.capitalize()} - {transaction_amount} - {transaction_description} - {transaction_date}")
def check_budget():
    total_expense = 0.0
    for transaction in transactions:
        if transaction[0] == "expense":
            total_expense += transaction[1]

    monthly_budget = get_valid_amount("Enter your monthly budget: ")

    print("\n--- BUDGET CHECK ---")
    print(f"Total Expenses: {total_expense}")
    print(f"Monthly Budget: {monthly_budget}")

    if total_expense > monthly_budget:
        amount_over = total_expense - monthly_budget
        print(f"WARNING: You are over budget by {amount_over}!")
    elif total_expense == monthly_budget:
        print("You have reached your monthly budget exactly.")
    else:
        amount_remaining = monthly_budget - total_expense
        print(f"You are within budget. Remaining: {amount_remaining}")
def view_by_category():
    category_totals = {}
    for transaction in transactions:
        if transaction[0] == "expense":
            category = transaction[2]
            amount = transaction[1]

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount
    print("\n---SPENDING BY CATEGORY---")
    if not category_totals:
        print("No expenses recorded yet.")
    else:
        for category, total in category_totals.items():
            print(f"{category}: {total}")
def edit_or_delete():
    if not transactions:
        print("No transactions to edit or delete.")
    else:
        print("\n--- ALL TRANSACTIONS ---")
        for index, transaction in enumerate(transactions, start=1):
            print(f"{index}. {transaction[0].capitalize()}- {transaction[1]}- {transaction[2]}- {transaction[3]}")
            
        chosen_number = get_valid_amount("Enter transaction number: ")
        chosen_index = int(chosen_number) - 1

        if chosen_index < 0 or chosen_index >= len(transactions):
            print("Invalid Transaction Number")
        else:
            action = input("Type 'edit' or 'delete': ").strip().lower()

            if action == "delete":
                transactions.pop(chosen_index)
                save_transactions()
                print("Transaction deleted.")
            elif action == "edit":
                new_amount = get_valid_amount("Enter a valid amount: ")
                transactions[chosen_index][1] = new_amount
                save_transactions()
                print("Transaction updated")
            else:
                print("Invalid action. No changes made.") 
##Each transaction is stored in a list format: [type, amount, description]
transactions = load_transactions()

running = True

while running:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add income")
    print("2. Add expense")
    print("3. View balance")
    print("4. View all transactions")
    print("5. Check budget")
    print("6. Exit")
    print("7. View spending by category")
    print("8. Edit/Delete a transaction")

    choice = input("Choose an option: ")
    ##choose if it's an income or expense.
    if choice == "1":
        add_transaction("income")
    elif choice == "2":
        add_transaction("expense")
    elif choice == "3":
        view_balance() 
    elif choice == "4":
        view_all_transactions() 
    elif choice == "5":
        check_budget()
    elif choice == "6":
        print("Goodbye!")
        running = False
        save_transactions()
    elif choice == "7":
        view_by_category()
    elif choice == "8":
        edit_or_delete() 
    else:
        print("Invalid option. Please choose a number from 1 to 8.") 
