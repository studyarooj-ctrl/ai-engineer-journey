# ==========================================
# 1. INITIAL VARIABLES (Basic Data Setup)
# ==========================================
balance = 5000.0        # Initial bank balance
total_expenses = 0.0   # Total kharcha count karne ke liye
correct_pin = 1234      # Correct PIN
pin_attempts = 3        # Maximum attempts allowed

print("=== WELCOME TO ATM & EXPENSE TRACKER ===")

# ==========================================
# 2. SECURITY CHECK (While loop + Break)
# ==========================================
is_logged_in = False    # Track karega ke user login hua ya nahi

while pin_attempts > 0:
    user_pin = int(input("Enter your 4-digit PIN: "))
    
    if user_pin == correct_pin:
        print("\nLogin Successful!\n")
        is_logged_in = True
        break  # Sahi PIN milte hi login loop khatam
    else:
        pin_attempts -= 1  # Arithmetic operator: attempt kam karein
        if pin_attempts > 0:
            print(f"Incorrect PIN! Attempts left: {pin_attempts}")
        else:
            print("\nAccount Locked! Too many wrong attempts.")

# ==========================================
# 3. MAIN MENU (Aapka Main Program)
# ==========================================
# Yeh block sirf tab chalega jab login successful hogar
while is_logged_in:
    print("---------------------------------")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Add Daily Expenses (For Loop)")
    print("5. Savings & Mini-Statement")
    print("6. Exit")
    print("---------------------------------")
    
    choice = input("Enter your choice (1-6): ")
    
    # --- Option 1: Check Balance ---
    if choice == "1":
        print(f"\nYour Current Balance is: ${balance}")
        
    # --- Option 2: Deposit Money ---
    elif choice == "2":
        deposit_amount = float(input("Enter amount to deposit: "))
        if deposit_amount > 0:  # Comparison operator
            balance += deposit_amount  # balance = balance + deposit_amount
            print(f"Successfully deposited ${deposit_amount}. New Balance: ${balance}")
        else:
            print("Invalid amount! Deposit must be greater than 0.")
            
    # --- Option 3: Withdraw Money ---
    elif choice == "3":
        withdraw_amount = float(input("Enter amount to withdraw: "))
        # Logical Operator (and) + Comparison Operator (<=, >)
        if withdraw_amount > 0 and withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"Please collect your cash. Remaining Balance: ${balance}")
        elif withdraw_amount > balance:
            print("Insufficient Balance!")
        else:
            print("Invalid amount! Amount must be greater than 0.")
            
    # --- Option 4: Add Daily Expenses (For Loop + Range + Continue) ---
    elif choice == "4":
        days = int(input("How many days of expenses do you want to add? "))
        
        # for loop aur range() ka use
        for day in range(1, days + 1):
            expense = float(input(f"Enter expense for Day {day}: "))
            
            # Agar negative ya zero entry ho to is din ko skip karein
            if expense <= 0:
                print("Invalid expense! Skipping this entry...")
                continue  # Loop agle day par chala jayega, neeche ka code run nahi hoga
            
            total_expenses += expense  # Valid expense ko total mein add karein
            
        print(f"\nExpenses recorded successfully! Total Expenses: ${total_expenses}")
        
    # --- Option 5: Savings & Report ---
    elif choice == "5":
        print("\n=== FINANCIAL REPORT ===")
        print(f"Current Balance: ${balance}")
        print(f"Total Expenses Logged: ${total_expenses}")
        
        # Balance aur expenses ka comparison
        if balance > total_expenses:
            remaining = balance - total_expenses
            print(f"Good job! You are in the savings zone. Effective Balance: ${remaining}")
        elif balance == total_expenses:
            print("Warning: Your expenses are equal to your balance!")
        else:
            print("Alert: Your expenses have exceeded your total balance!")
            
    # --- Option 6: Exit ---
    elif choice == "6":
        print("\nThank you for using our service. Goodbye!")
        break  # Main menu loop ko stop kar dega
        
    # Invalid choice handler
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")