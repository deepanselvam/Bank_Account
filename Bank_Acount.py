class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,initial_amount,acc_name):
        self.balance=initial_amount
        self.name=acc_name
        print(f"Account '{self.name}' Cereted \n Balance =${self.balance:.2f}")

    def get_balance(self):
        print(f"Account '{self.name}'\n Balance =${self.balance:.2f}")

    def deposit(self,amount):
        self.balance=self.balance+amount    
        print('\nDeposit Complete') 
        self.get_balance()

    def viable_transaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(f"Sorry , Account {self.name} only has a balance of ${self.balance:.2f}")

    def withdraw(self,amount):    
        try:
            self.viable_transaction(amount)
            self.balance=self.balance-amount
            print('\n withdraw complete.')
            self.get_balance()

        except BalanceException as error:
            print(f"\n withdraw interrupted:{error}")  

    def transfer(self,amount,account):
        try:
            print('\n *************\n\nBegining Transfer..💨')
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Completed! ✅ \n\n***************")
        except BalanceException as error:
            print(f'\nTransfer Interupted.❌ {error}')    


class InterestRewardAcc(BankAccount):
      def deposit(self, amount):
          return super().deposit(amount*1.05)
      print(f'\n Deposit Completed')


class Saving_Acc(BankAccount):
    
    def __init__(self,initial_amount,acc_name):
        super().__init__(initial_amount,acc_name)
        print(f"Savings Account '{self.name}' Cereted \n Balance =${self.balance:.2f}")
        self.fee=5
    def withdraw(self, amount):
       try:
           self.viable_transaction(amount+self.fee)
           self.balance=self.balance-(amount+self.fee)
           print("\n Withdraw Completed.")
           self.get_balance()

       except BalanceException as error:
           print(f'\n withdraw interrupted:{error}')   