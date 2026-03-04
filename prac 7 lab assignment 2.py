balance = 0

def show_balance():
    print("Current Balance:", balance)

def deposit():
    global balance
    amt = float(input("Enter amount to deposit: "))
    balance += amt
    print("Amount Deposited")

def withdraw():
    global balance
    amt = float(input("Enter amount to withdraw: "))
    if amt <= balance:
        balance -= amt
        print("Amount Withdrawn")
    else:
        print("Insufficient Balance")

while True:
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    ch = int(input("Enter choice: "))
    
    if ch == 4:
        break
    elif ch == 1:
        show_balance()
    elif ch == 2:
        deposit()
    elif ch == 3:
        withdraw()