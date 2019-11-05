"""
Assignment 5 - OOP Bank Account Test

This file contains all the test scenerios checked for Assignment 5
"""

#import pytest - not needed due to using virtual environment on PC
from datetime import datetime
from banking import Transaction, Account

def test_account_setup():
    """
    This test checks that the amount parameter is bound to self
    """

    becky_account = Transaction(100)
    assert becky_account.get_account() == 100

def test_account_setup_float():
    """
    This test checks that the amount parameter is bound to self when using a
    float
    """

    becky_account = Transaction(100.01)
    assert becky_account.get_account() == 100.01

def test_account_setup_decimal():
    """
    This test checks that the amount parameter is bound to self
    """

    becky_account = Transaction(100.0)
    assert becky_account.get_account() == 100.0

def test_timestamp():
    """
    This test checks that the timestamp is bound to self
    """

    becky_account = Transaction(100, datetime(2018, 1, 1, 0, 0, 0))
    assert becky_account.get_timestamp() == datetime(2018, 1, 1, 0, 0, 0)

def test_bank_entry():
    """
    This test returns a string with the transaction bank_entry
    """

    becky_account = Transaction(1234.56, datetime(2019, 1, 1))
    assert becky_account.bank_entry() == "2019-01-01: +$1234.56"

def test_zero_balance():
    """
    This test checks that the balance is 0 when there are no transactions
    """
    becky_account = Account(0)
    assert becky_account.get_balance() == 0
