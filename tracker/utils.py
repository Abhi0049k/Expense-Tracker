import csv
from datetime import date, time
from .transactions import Transaction
from .enum import Cashflow_Type, Category

def get_cashflow_type():
    while True:
        user_input = input("Enter transaction type [Income/Expense (I/E)]: ").strip().lower()
        if user_input in ("income", "i"):
            return Cashflow_Type.INCOME
        elif user_input in ("expense", "e"):
            return Cashflow_Type.EXPENSE
        else:
            print("Invalid input. Please type 'Income/I' or 'Expense/E'.")

def get_category():
    print("\nAvailable Categories:")
    for idx, category in enumerate(Category, start=1):
        print(f"{idx}. {category.value.title()}")

    while True:
        user_input = input("Select a category by number or name: ").strip().lower()

        if user_input.isdigit():
            idx = int(user_input)
            if 1 <= idx <= len(Category):
                return list(Category)[idx - 1]
            else:
                print("Invalid number. Please choose a valid index.")
        else:
            normalized_input = user_input.replace(" ", "")
            for category in Category:
                if normalized_input == category.value.lower():
                    return category
            print("Invalid category name. Please try again.")
            
def save_to_csv(transactions):
    with open("transaction.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Amount", "Title", "Type", "Category", "Date", "Time"])
        for t in transactions:
            writer.writerow([
                t.id,
                t.amount,
                t.title,
                t.cashflow_type,
                t.category,
                t.date.isoformat(), 
                t.time.isoformat()
            ])
    print("Transactions saved to CSV!")
    
    
def load_from_csv():
    transactions = []
    try:
        with open("transaction.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                transaction = Transaction(
                    id=int(row["ID"]),
                    amt=float(row["Amount"]),
                    title=row["Title"],
                    cashflow_t=Cashflow_Type(row["Type"].lower()).value.lower(), 
                    category=Category(row["Category"].lower()).value.lower(),      
                    date=date.fromisoformat(row["Date"]), 
                    time=time.fromisoformat(row["Time"])  
                )
                transactions.append(transaction)
    except FileNotFoundError:
        print("File Not Found!")
    return transactions