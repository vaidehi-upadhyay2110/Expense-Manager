# ------------------------------
# SIMPLE EXPENSE MANAGER (BASIC)
# ------------------------------

# Load expenses from file
def load_expenses():
    expenses = []
    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                amount, category, desc, date = line.strip().split("|")
                expenses.append({
                    "amount": float(amount),
                    "category": category,
                    "description": desc,
                    "date": date
                })
    except:
        pass
    return expenses


# Save expenses to file
def save_expenses(expenses):
    with open("expenses.txt", "w") as f:
        for e in expenses:
            line = f"{e['amount']}|{e['category']}|{e['description']}|{e['date']}\n"
            f.write(line)


# Load budget
def load_budget():
    try:
        with open("budget.txt", "r") as f:
            return float(f.read())
    except:
        return 0.0


# Save budget
def save_budget(amount):
    with open("budget.txt", "w") as f:
        f.write(str(amount))


# ------------------------------
# FUNCTIONS
# ------------------------------

def add_expense():
    print("\n--- Add Expense ---")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    desc = input("Enter description: ")
    date = input("Enter date (YYYY-MM-DD): ")

    expenses = load_expenses()

    expense = {
        "amount": amount,
        "category": category,
        "description": desc,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added!\n")


def monthly_summary():
    print("\n--- Monthly Summary ---")

    import datetime
    today = datetime.date.today()
    month = today.month
    year = today.year

    expenses = load_expenses()

    if len(expenses) == 0:
        print("No expenses found.\n")
        return

    total = 0
    category_total = {}

    for e in expenses:
        y, m, d = map(int, e["date"].split("-"))
        if y == year and m == month:
            total += e["amount"]

            cat = e["category"]
            if cat not in category_total:
                category_total[cat] = 0
            category_total[cat] += e["amount"]

    budget = load_budget()
    remaining = budget - total

    print("\nTotal spent this month:", total)
    print("Category-wise totals:")
    for c, v in category_total.items():
        print(f"  {c}: {v}")

    print("\nBudget:", budget)
    print("Remaining:", remaining)
    print()


def set_budget():
    print("\n--- Set Budget ---")
    b = float(input("Enter monthly budget: "))
    save_budget(b)
    print("Budget updated!\n")


# ------------------------------
# MENU
# ------------------------------

def main():
    while True:
        print("===== EXPENSE MANAGER =====")
        print("1. Add Expense")
        print("2. Monthly Summary")
        print("3. Set Budget")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            monthly_summary()
        elif choice == "3":
            set_budget()
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice\n")


main()