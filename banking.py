"""
Assingment 5 - OOP Bank Account

Defines account and transaction functions and updates entries made with amounts
and optional timestamps
"""

from dataclasses import dataclass
from decimal import getcontext, Decimal
import datetime

#set decimal point precision to 2 places
getcontext().prec = 3

@dataclass
class Transaction:
    """
    This class stores the bank account balance and any associated timestamps
    """

    amount: int or float or Decimal
    timestamp: datetime

    def __init__(self, amount, timestamp = None):
        self.amount = amount
        self.timestamp = timestamp

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
        if self.timestamp is None:
            self.timestamp = datetime.now()
        return self.timestamp
