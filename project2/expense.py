
print("========== EXPENSE TRACKER ==========")

total_expense = 0

while True:
    purpose = input("\nEnter Expense Purpose (or type 'done' to finish): ")

    if purpose.lower() == "done":
        break

    amount = float(input("Enter Amount: ₹"))

    total_expense += amount

    print(f"Expense Added: {purpose} - ₹{amount}")

print("\n========== EXPENSE SUMMARY ==========")
print("Total Amount Spent: ₹", total_expense)
print("Thank You for Using Expense Tracker!")