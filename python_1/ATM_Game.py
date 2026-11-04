
# Starting bank balance
balance = 100

# Welcome message
print("Welcome to the Mini ATM!")

# Keep the ATM running until the user exits
while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit"

    # Ask the user what they want to do
    choice = input("Choose an option (1-4): ")

    # Check the account balance
    if choice == "1":
        print("Your balance is $", balance)

    # Add money to the account
    elif choice == "2":
        amount = float(input("How much do you want to deposit? "))
        if amount > 0:
            balance = balance + amount
            print("Deposit successful!")
        else:
            print("Enter a positive amount.")

    # Withdraw money from the account
    elif choice == "3":
        amount = float(input("How much do you want to withdraw? "))
        if amount <= 0:
            print("Enter a positive amount.")
        elif amount <= balance:
            balance = balance - amount
            print("Withdrawal successful!")
        else:
            print("Not enough money!")

    # Exit the ATM
    elif choice == "4":
        print("Thank you for using the ATM!")
        break

    # Handle invalid choices
    else:
        print("Invalid option.")
