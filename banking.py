# ATM
balance = 0
trancHis = []

def trans():
    if len(trancHis) == 0:
        print("No transactions yet.")
    else:
        print("\n--- Transaction History ---")
        for i in trancHis:
            print(i)

def balanc():
    global balance
    print(f"Balance : ₹{balance}")

def depositmoney():
    global balance
    m = int(input("Enter amount : ₹"))
    balance = balance + m
    trancHis.append(f"Deposited  : ₹{m}")
    print(f"₹{m} Added successfully!")

def withdral():
    global balance
    withdAmt = int(input("Enter withdrawal amount : ₹"))
    if withdAmt > balance:
        print("Insufficient balance")
    else:
        balance -= withdAmt
        trancHis.append(f"Withdrawn  : ₹{withdAmt}")
        print(f"₹{withdAmt} withdrawal successful")

def atm():
    while True:
        print("\n--- Welcome ---\n")
        print("1. Show balance")
        print("2. Deposit money")
        print("3. Withdrawal")
        print("4. Transaction History")
        print("5. Exit")
        choice = int(input("\nEnter choice : "))
        if choice == 1:
            balanc()
        elif choice == 2:
            depositmoney()
        elif choice == 3:
            withdral()
        elif choice == 4:
            trans()
        elif choice == 5:
            print("Thank You!")
            break
        else:
            print("Enter valid number")

atm()