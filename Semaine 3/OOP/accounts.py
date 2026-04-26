import datetime
import pytz

class Account:
    """ Simple account class with balance"""
 
    @staticmethod
    def _current_time():
        return datetime.datetime.now(datetime.UTC)
    
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
        self.__transaction_list = [(Account._current_time(), balance)]
        print("Account created for {} with balance of {}".format(self.__name, self.__balance))
    
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
        else:
            self.__balance += amount
            self.__transaction_list.append((Account._current_time(), amount))
            print("Deposit accepted, balance is now {}".format(self.__balance))
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
            self.__transaction_list.append((Account._current_time(), -amount))
            print("Withdrawal accepted, balance is now {}".format(self.__balance))

    def show_balance(self):
        print("Balance for {} is {}".format(self.__name, self.__balance))

    def show_transactions(self):
        for date, amount in self.__transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:                
                tran_type = "withdrew"
                amount *= -1
            print("{:6} {} on {} local time was {}".format(amount, tran_type, date, date.astimezone()))

if __name__ == "__main__":
    tim = Account("Tim", 0)
    tim.deposit(1000)
    tim.show_balance()
    tim.withdraw(500)
    tim.show_balance()
    tim.withdraw(600)
    tim.show_transactions()
    
    steph = Account("Steph", 800)
    steph.deposit(200)
    steph.show_balance()
    steph.withdraw(100)
    steph.show_balance()
    steph.__balance = 10000
    steph.show_balance()
    steph.show_transactions()
    print(steph.__dict__)