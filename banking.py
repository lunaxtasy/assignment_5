"""
Assingment 5 - OOP Bank Account

Defines account and transaction functions and updates entries made with amounts
and optional timestamps
"""

from dataclasses import dataclass
from decimal import getcontext, Decimal
from datetime import datetime, date

#set decimal point precision to 2 places
getcontext().prec = 3

@dataclass
class Transaction:
    """
    This class stores the bank account balance and any associated timestamps
    """

    amount: int or float or Decimal
    timestamp: datetime

    def __init__(self, amount, timestamps=None):
        self.amount = amount
        self.timestamps = timestamps

    def __str__(self):
        """
        Returns transaction entry
        """
        return self.bank_entry()

    def __repr__(self):
        """
        Allows reprinting of an object

        If I had the timestamp stuff figured out, I would probably be using
        that instead
        """
        return f"Transaction(timestamps = {self.timestamps}, amount = {self.amount})"

    def get_account(self):
        """
        This function initiates the acquiring of an account using an amount of
        money
        """
        return self.amount

    def get_timestamp(self):
        """
        This function gets the timestamp for a transaction
        """
        if self.timestamps is None:
            self.timestamps = date.now()
        return self.timestamps

    def bank_entry(self):
        """
        Creates entry for transaction list
        """
        return f'{self.timestamps.strftime("%Y-%m-%d")}: +${self.amount}'

class Account:
    """
    This class allows for deposits and withdrawals and calculates balance, as
    well as showing a list of transactions
    """

    def __init__(self, account_balance=0):
        self.account_balance = account_balance
        self.transactions = {}

    def get_balance(self):
        """
        Returns the current acccount get_balance
        """
        return self.account_balance
