from datetime import datetime
from .utils import load_from_csv, get_cashflow_type, get_category
from .transactions import Transaction
from .enum import Cashflow_Type

class Finance_Tracker:
    def __init__(self):
        self.transactions = load_from_csv()
        self.next_id = len(self.transactions)+1 if len(self.transactions) == 0 else self.transactions[len(self.transactions)-1].id+1
    
    def add_transaction(self):
        note = input("Enter a note about the transaction: ");
        try:
            amt = int(input("Enter amount spend: "))
        except ValueError:
            print("Invalid Amount. Must be a number.")
            return
        if amt <= 0:
            print("Amount must be positive")
            return
        c_type = get_cashflow_type().value     
        cgt = get_category().value
        
        new_trans= Transaction(id = self.next_id, amt = amt, title = note, cashflow_t= c_type, category=cgt)
        print(new_trans)
        self.transactions.append(new_trans);
        self.next_id+=1
        print("Transaction added!")
        
    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
            return
        
        for transaction in self.transactions:
            print(transaction.id, transaction.amount, transaction.title, transaction.date, transaction.time, transaction.cashflow_type, transaction.category)
    
    def delete_transaction(self):
        try:
            transaction_id = int(input("Enter Id of the transaction to delete: "))
        except ValueError:
            print("Invalid ID. Must be a number.")
            return 
        for idx, transaction in enumerate(self.transactions):
            if transaction.id == transaction_id:
                self.transactions.pop(idx)
                print("Transaction deleted!")
                return
            
        print(f"No transaction found with ID: {transaction_id}")
        
    def edit_transaction(self):
        try:
            transaction_id = int(input("Enter ID of transaction to edit: "))
        except ValueError:
            print("Invalid ID. Must be a number")
            return
        
        for transaction in self.transactions:
            if transaction.id == transaction_id:
                print("Leave blank to keep current value.")
                note = input(f"New note (current: {transaction.title}): ")
                new_amount = input(f"New amount (current: {transaction.amount}): ")
                new_category = get_category()
                new_type = get_cashflow_type()
                
                if note:
                    transaction.title = note
            
                if new_amount:
                    transaction.amount = new_amount
                
                if new_category:
                    transaction.category = new_category
                
                if new_type:
                    transaction.cashflow_type = new_type
                print("Transaction Updated!")
                return
        print(f"No transaction found with ID {transaction_id}")

    def get_balance(self):
        income = sum(t.amount for t in self.transactions if t.cashflow_type == Cashflow_Type.INCOME.value)
        expense = sum(t.amount for t in self.transactions if t.cashflow_type == Cashflow_Type.EXPENSE.value)
        print(f"Income: ₹{income:.2f}")
        print(f"Expenses: ₹{expense:.2f}")
        print(f"Net Balance: ₹{income - expense:.2f}")
        
    def summarize_by_category(self):
        summary = {}
        for t in self.transactions:
            if t.cashflow_type == Cashflow_Type.EXPENSE.value:
                key = t.category
                summary[key] = summary.get(key, 0) + t.amount
        for category, total in summary.items():
            print(f"{category}: ₹{total:.2f}")
    
    def filter_transactions(self):
        print("Filter by:\n1. Category\n2. Date\n3. Type")
        choice = input("Enter your choice: ").strip()
        filtered = []

        if choice == "1":  # Category
            category = get_category()
            filtered = [t for t in self.transactions if t.category == category.value]
        elif choice == "2":
            date_str = input("Enter date (YYYY-MM-DD): ")
            target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            filtered = [t for t in self.transactions if t.date == target_date]
        elif choice == "3":  
            cft = get_cashflow_type()
            filtered = [t for t in self.transactions if t.cashflow_type == cft.value]
        
        for t in filtered:
            print(t)