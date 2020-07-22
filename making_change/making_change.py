#!/usr/bin/python

import sys


def making_change(amount, denominations):
    number_of_ways = 0

    def remove_coin(total, value):
        nonlocal number_of_ways
        total -= value
        if total < 0:
            return
        elif total == 0:
            number_of_ways += 1
        else:
            for value in denominations:
                remove_coin(total, value)
    if amount <= 1:
        return 1
    else:
        remove_coin(amount, 0)


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    amount = 10
    denominations = [1, 5, 10, 25, 50]
    if len(sys.argv) > 1:
        amount = int(sys.argv[1]) 
    print("There are {ways} ways to make {amount} cents.".format(
        ways=making_change(amount, denominations), amount=amount))
