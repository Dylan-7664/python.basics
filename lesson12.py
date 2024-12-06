class Account:
    def __init__(self, full_name, acc_no, phone ,balance):
        self.full_name = full_name
        self.acc_no = acc_no
        self.phone = phone
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print(f'amount {amount} deposited successfully to account {self.acc_no}')

    def withdraw(self, amount):
        if self.balance <= amount:
            print(f'insufficient funds. Balance is {self.balance}')
        else:
            self.balance -= amount
            print(f'Amount {amount} withdrawn successfully from account {self.acc_no}')

    def check_balance(self):
        print(f'Balance for account {self.acc_no} is: {self.balance}')

kevo_acc = Account("Kevin Maina", "0001", "0712222333", 1000)
sara_acc = Account("Sarah Hassan", "002", "0723432234", 1800)
willy_account = Account(balance=8000, acc_no='003', full_name="Will Jones", phone="0744556677")

kevo_acc.deposit(2000)
kevo_acc.check_balance()
kevo_acc.withdraw(500)
kevo_acc.check_balance()

sara_acc.deposit(1000)
sara_acc.check_balance()

willy_account.deposit(500)
willy_account.check_balance()



