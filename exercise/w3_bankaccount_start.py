# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:54:59 2019

@author: Fabrizio
"""
class BankAccount:

    def __init__(self,iban,holder_name):
        self.iban = iban
        self.holder_name = holder_name
        self.balance = 0

    def __repr__(self):
        return (
            f'BankAccount(iban="{self.iban}", '
            f'holder_name="{self.holder_name}", '
            f'balance={self.balance})')
    
    def deposit(self, amount):
        self.balance += amount
        return f'Deposited {amount}, current balance is {self.balance}'
    
    def withdraw(self, amount):
        self.balance -= amount
        return f'Withdrew {amount}, current balance is {self.balance}'

class MinimumBalanceAccount(BankAccount):
    
    def __init__(self, iban, holder_name, minimum_balance):
        """
        Inizialize an employee
        """
        # initialize the values of the superclass
        super().__init__(iban, holder_name)
        # initialize the values of the subclass
        self.minimum_balance = minimum_balance
        
    def withdraw(self, amount):
        if (self.balance - amount) >= self.minimum_balance:
            super().withdraw(amount)
            return f'Withdrew {amount}, current balance is {self.balance}'
        else:
            return f"Not enough funds to withdraw {amount}"
    

    pass
    
if __name__=='__main__':

    ba1 = BankAccount(123,'Fabrizio')
    print(ba1)
    operation = ba1.deposit(1000)
    print(operation)
    print(ba1)
    ba2 = MinimumBalanceAccount(234,'Iozzi',minimum_balance=100)
    print(operation)
    print(ba2)
    operation = ba2.deposit(1000)
    print(operation)
    print(ba2)
    operation = ba2.withdraw(500)
    print(operation)
    print(ba2)
    operation = ba2.withdraw(500)
    print(operation)
    print(ba2)
    

