import json
import os

category = {"Network", "Software", "Hardware", "Other"}
urgency = {"High", "Medium", "Low"}

def create_ticket(title, category, urgency, users):
    if not isinstance(title, str) or title == " ".strip():
        raise TypeError("Enter a valid ticket title")
    if category not in category:
        raise ValueError(f"Enter a valid category: {category}")
    if urgency not in urgency:
        raise ValueError(f"Enter a valid urgency: {urgency}")
    if not isinstance(users, int) or users <= 0:
        raise TypeError("Enter a positive integer")
    ticket = {
        "title": title.strip().capitalize(),
        "category": category.strip().capitalize(),
        "urgency": urgency.strip().capitalize(),
        "users": users,
    }
    return ticket
def save_ticket(ticket):
    try:
        with open("ticket.json","r") as file:
            tickets = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tickets = []
    if not isinstance(tickets, list):
        tickets = []
    tickets.append(ticket)
    with open("ticket.json","w") as file:
        json.dump(tickets, file)
print("===== Welcome to campus flow help desk =====")
title = input("Enter ticket title: ").strip()
category = input("Enter ticket category: ").strip()
urgency = input("Enter ticket urgency: ").strip()
users = int(input("Enter number of affected users: "))

ticket = create_ticket(title, category, urgency, users)
save_ticket(ticket)
print("Ticket created successfully:")
print(json.dumps(ticket))