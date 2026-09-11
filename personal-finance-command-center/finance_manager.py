##This program keeps track of your income and expenses
##The aim is to make sure you know where every dime you spend goes 
## and how you spend it and on what.

##Transaction data racord begins here

transactions = []

transaction = [] 

transaction_amount = float(input("Enter amount: ")) 
transaction_type = input("Enter your transaction type: ") 
description = input("Enter description: ") 
transaction.append(transaction_amount)
transaction.append(transaction_type)
transaction.append(description) 
transactions.append(transaction) 
print(transactions)

total_income = 0 
for transaction in transactions:
    if transaction_type == "income":
        final_income = transaction_amount + total_income 
print(final_income)

total_expense = 0
for transaction in transactions:
    if transaction_type == "expense":
        final_expense = transaction_amount + total_expense
print(final_expense) 