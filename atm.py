print("WELCOME TO ATM 🙏")
acc = input("Enter your account number: ")
pin = input("Enter your PIN: ")
balance=1000
while True:
    print("\nATM Menu:")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        print("Your balance is: ", balance)
    elif choice == '2':
        amount = float(input("Enter the deposit amount: "))
        balance += amount
        print("DEPOSIT SUCCESSFUL")
        print("Your New Balance is: ", balance)
    elif choice == '3':
        amount = float(input("Enter the withdrawal amount: "))
        if amount > balance:
            print("INSUFFICIENT FUNDS")
        else:
            balance -= amount
            print("SUCCESSFUL WITHDRAWAL")
            print("NEW BALANCE IS: ", balance)
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!🙏")
        break
    else:
        print("Invalid choice. Please enter a valid option.")


