###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

check_pin = input('Enter PIN to check: ')
if check_pin == pin:

    while True:
        print()
        print("ATM Menu:")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print('4. Change PIN')
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            print(f"Your current balance is: €{balance}")

        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            balance += amount
            print(f"€{amount} has been deposited. New balance: €{balance}")

        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"€{amount} has been withdrawn. New balance: €{balance}")
            else:
                print("Insufficient balance.")

        elif choice == '5':
            print("Exiting... Thank you for using the ATM!")
            break  # Exit the loop

        elif choice == '4':
            new_pin = input('Enter a new 4-digit PIN: ')
            if new_pin.isdigit and len(new_pin) == 4:
                pin = new_pin
                print('PIN has been successfully changed.')
            else:
                 print("Invalid PIN. Please enter exactly 4 digits.")

        else:
            print("Invalid option. Please try again.")

else:
    print('Sorry, wrong PIN...')