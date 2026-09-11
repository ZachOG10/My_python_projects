# LEVEL 1 — TRANSACTION STORAGE

transactions = []

# Ask how many transactions to enter
num_transactions = int(input("How many transactions would you like to enter? "))

for i in range(num_transactions):
    print(f"\n--- Transaction {i + 1} ---")
    transaction_type = input("Enter transaction type (income/expense): ").strip().lower()
    transaction_amount = float(input("Enter amount: "))
    description = input("Enter category/description: ")
    
    # Store transaction details
    transaction = [transaction_type, transaction_amount, description]
    transactions.append(transaction)

# LEVEL 2 — FINANCIAL CALCULATIONS

total_income = 0.0
total_expenses = 0.0

for transaction in transactions:
    # transaction[0] is type, transaction[1] is amount
    if transaction[0] == "income":
        total_income += transaction[1]
    elif transaction[0] == "expense":
        total_expenses += transaction[1]

# Balance = Income - Expenses
balance = total_income - total_expenses

print("\n--- FINANCIAL SUMMARY ---")
print(f"Total Income: {total_income}")
print(f"Total Expenses: {total_expenses}")
print(f"Balance: {balance}")

# LEVEL 3 — FINANCIAL DECISIONS

monthly_budget = float(input("\nEnter your monthly budget: "))

print("\n--- BUDGET CHECK ---")
if total_expenses > monthly_budget:
    amount_over = total_expenses - monthly_budget
    print(f"WARNING: You are over budget by {amount_over}!")
elif total_expenses == monthly_budget:
    print("You have reached your monthly budget.")
else:
    remaining_budget = monthly_budget - total_expenses
    print(f"Remaining budget: {remaining_budget}")

print("\n--- BALANCE CHECK ---")
if balance > 0:
    print("Your balance is positive.")
elif balance == 0:
    print("You have broken even.")
else:
    print("Your balance is negative.")