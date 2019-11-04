"""
Assingment 5 - OOP Bank Account

Defines account and transaction functions and updates entries made with amounts
and optional timestamps
"""

from dataclasses import dataclass

@dataclass
class Transaction:
    """
    This class stores the bank account balance and any associated timestamps
    """

    amount: int or float or decimal

    def __init__(self, amount):
        self.amount = amount

    def get_account(self):
        """
        This function initiates the acquiring of an account using an amount of
        money
        """
        return self.amount
