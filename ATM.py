class bankdetails:
    def __init__(self,balance=0):
        self.balance=balance
        print(f"\n----Welcome to ATM----")
    def deposit(self,amount):
        self.balance+=amount
        print(f"your deposit amount is {amount}")
    def withdraw_amount(self,amount):
        if self.balance >= amount:
            self.balance-=amount
            print(f"your withdraw amount is {amount}")
        else:
            print("invalid balance")
    def transfer_money(self,amount):
        if self.balance >= amount:
            self.balance-=amount
            print(f"your transfer amount is {amount}")
        else:
            print("invalid balance")
    def check_balance(self):
        print(f"your current balance amount is {self.balance}")
bankdel=bankdetails(500)
def allwew():
    print("Please enter your 4-digit PIN number to proceed.")
    PIN_number=int(input("Enter the 4-digit PIN Number:"))
    while True:
            print("\n--- ATM MENU ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transfer Money")
            print("5. Exit")
            Transaction=int(input("The user selects the type of transaction 1 to 5:"))
            if Transaction == 1:
                bankdel.deposit(int(input("")))
            elif Transaction == 2:
                bankdel.withdraw_amount(int(input("")))
            elif Transaction == 3:
                bankdel.check_balance()
            elif Transaction == 4:
                bankdel.transfer_money(int(input("")))
            elif Transaction == 5:
                print("your transaction is complete") 
                break
            else:
                print("Invalid selection. Please try again.")
if __name__ == "__main__":
    allwew()
