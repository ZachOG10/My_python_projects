##This program keeps track of your income and expenses
##The aim is to make sure you know where every dime you spend goes 
## and how you spend it and on what.

##This blocks of code stores the transactions carried out by the user

transactions = []

transaction = [] 

transaction_amount = float(input("Enter amount: ")) 
transaction_type = input("Enter your transaction type(income/expense): ") 
description = input("Enter description: ") 
transaction.append(transaction_amount)
transaction.append(transaction_type)
transaction.append(description) 
transactions.append(transaction) 
print(transactions)

## This blocks of code calculates the income, expense of user

total_income = 0
total_expense = 0
for transaction in transactions:
    if transaction[1] == "income":
        total_income = transaction[0] + total_income
    if transaction[1] == "expense":
        total_expense = transaction[0] + total_expense
total_balance = total_expense - total_income
print(total_income)
print(total_expense)
print(total_balance)

##The following blocks of code determines the 
## financial status of the user 
monthly_budget = float(input("Enter your budget for the month: "))

print("total_expence:", total_expense)
print("monthly_budget:", monthly_budget)

if total_expense > monthly_budget:
    budget_exceeded = monthly_budget - total_expense
    print("WARNING: You have exceeded your monthly budget!")
elif total_expense == monthly_budget:
    print("You have reached your monthly budget.")
else:
    budget_remaining = monthly_budget - total_expense 
    print("You are within your budget.")

##This blocks of code prints the balance condition
balance = total_balance 
if balance > 0:
    print("Your balance is positive")
elif balance == 0:
    print("You have broken even")
elif balance < 0:
    print("Your balance is negative")
