"""
Assignment 5 - OOP Bank Account Test

This file contains all the test scenerios checked for Assignment 5
"""

#import pytest - not needed due to using virtual environment on PC
from banking import Transaction

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
