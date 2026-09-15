"""
THIS IS MY FIRST PROJECT SINCE I LEANT PYTHON.
AN EXPENSE TRACKER 
This program keeps track of your income and expenses.
It helps you know exactly where your money goes.
"""

##This list stores all transactions.
##Each transaction is stored as a list: [type, amount, description]
transactions = []

running = True

while running:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add income")
    print("2. Add expense")
    print("3. View balance")
    print("4. View all transactions")
    print("5. Check budget")
    print("6. Exit")

    choice = input("Choose an option: ")

    ##Add if it's an income or expense.
    if choice == "1" or choice == "2":
        if choice == "1":
            transaction_type = "income"
        elif choice == "2":
            transaction_type = "expense"

        transaction_amount = float(input("Enter amount: "))
        description = input("Enter category/description: ")

        ##Store the  current transaction as [type, amount, description]
        transaction = [transaction_type, transaction_amount, description]
        transactions.append(transaction)

        print(f"{transaction_type.capitalize()} of {transaction_amount} added.")

    ##This block allows you view your balance.
    elif choice == "3":
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

    ##This block allows you to view all transactions.
    elif choice == "4":
        if not transactions:
            print("No transactions recorded yet.")
        else:
            print("\n--- ALL TRANSACTIONS ---")
            for index, transaction in enumerate(transactions, start=1):
                t_type = transaction[0]
                t_amount = transaction[1]
                t_description = transaction[2]
                print(f"{index}. {t_type.capitalize()} - {t_amount} - {t_description}")

    ##This block stores your budget and tells you when you exceed your budget or not.
    elif choice == "5":
        total_expense = 0.0
        for transaction in transactions:
            if transaction[0] == "expense":
                total_expense += transaction[1]

        monthly_budget = float(input("Enter your monthly budget: "))

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

    ##This block exits the while loop. 
    elif choice == "6":
        print("Goodbye!")
        running = False

    ##If you enter an invalid choice the program sends you this message
    else:
        print("Invalid option. Please choose a number from 1 to 6.")