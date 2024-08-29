"""
Banking
    Attributes - acc_no,name,account_type,balance,branch
    Methods - display(), 

Menu
1) Add a account
    acc_no = INT
    name = STR
    account_type = STR (saving/current)
    balance
    branch = STR
    x = Banking(acc_no,name,account_type,branch)
2) Display all account
    - All account display
3) Check Balance of a account
4) Deposit Balance
5) Withdraw money
6) Exit
"""

from typing import List


class banking_app:

    def __init__(self, acc_no: int, name: str, branch: str, accType: str):
        self.acc_no = acc_no
        self.name = name
        self.branch = branch
        self.accType = accType
        self.balance = 0

    def get_balance(self) -> int:
        return self.balance

    def deposite(self, amount) -> int:
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance

    def Display_all_acc(self):
        print(f"acc_no = {self.acc_no}")
        print(f"Name = {self.name}")
        print(f"branch = {self.branch}")
        print(f"accType = {self.accType}")
        print(f"balance = {self.balance}\n\n")


bank_acc_details: List[banking_app] = []

while True:
    print("1) add an account")
    print("2) Display all account")
    print("3) Display bank balance")
    print("4) Deposit money")
    print("5) Withdraw money")
    print("6) exit")

    choice = int(input("enter choice: \n\n"))

    if choice == 1:
        acc_no = int(input("enter account number: "))
        name = input("enter name: ")
        while True:
            accType = input("enter account type: ")
            if accType == "saving" or accType == "current":
                break
            else:
                print("Invalid  accType, please enter saving/current")
        branch = input("enter branch name: ")
        x = banking_app(acc_no, name, branch, accType)
        bank_acc_details.append(x)
    elif choice == 2:
        if len(bank_acc_details) == 0:
            print("no bank acc found")
        else:
            for acc in bank_acc_details:
                acc.Display_all_acc()
    elif choice == 3:
        ac_no = int(input("enter account number: "))
        for acc in bank_acc_details:
            if acc.acc_no == ac_no:
                print(f"Your balance is : {acc.get_balance()}")
    elif choice == 4:
        ac_no = int(input("enter account number to deposite into: "))

        for acc in bank_acc_details:
            if acc.acc_no == ac_no:
                amount = int(input("enter deposite money amount: "))
                print(
                    f"{amount} has been deposited to your ccount. Updated balance: {acc.deposite(amount)}\n"
                )
    elif choice == 5:
        ac_no = int(input("enter account number to withdraw from: "))
        for acc in bank_acc_details:
            if acc.acc_no == ac_no:
                amount = int(input("enter withdrawal money amount: "))
                if amount <= acc.balance:
                    print(
                        f"{amount} has been debited to your account. Available balance: {acc.withdraw(amount)}\n"
                    )
                else:
                    print("Insuficient Balance\n")
    elif choice == 6:
        break
    else:
        print("Invalid choice")
