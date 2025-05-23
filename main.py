from tracker.finance_tracker import Finance_Tracker
from tracker.utils import save_to_csv

def display_menu():
    print("\n=== Expense Tracker Menu ===")
    print("1. Add a Transaction")
    print("2. View All Transactions")
    print("3. Store Transaction Note")
    print("4. Delete a Transaction")
    print("5. Edit Transaction Details")
    print("6. View Balance Summary")
    print("7. View Spending by Category")
    print("8. Filter Transactions")
    print("9. Exit")

tracker = Finance_Tracker() 

while True:
    try:
        display_menu()
        choice = input("\nEnter your choice (1-9): ").strip()

        if choice == "1":
            tracker.add_transaction()
        elif choice == "2":
            tracker.show_transactions()
        elif choice == "3":
            save_to_csv(transactions=tracker.transactions)
        elif choice == "4":
            tracker.delete_transaction()
        elif choice == "5":
            tracker.edit_transaction()
        elif choice == "6":
            tracker.get_balance()
        elif choice == "7":
            tracker.summarize_by_category()
        elif choice == "8":
            tracker.filter_transactions()
        elif choice == "9":
            print("\nExiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")
    except KeyboardInterrupt:
        print("\nExiting... Goodbye!")
        break