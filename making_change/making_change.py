#!/usr/bin/python

import sys


# def making_change(amount, denominations):
#     cache = {0: 1}
#     count = 0
#     # If it's in the cache, return its count
#     # Otherwise, calculate its value and add it to the cache
#     if amount in cache:
#         return cache[amount]
#     else:
#         pass
#         # Remove the largest coin value
#         # Continue until we hit zero, then increment count
#         # Every branch represents a new value to add to the cache

#         # Remove 10, get 0.
#             # Set the value of 10 to be 1 in the cache
#         # Remove 5, get 5.
#             # Wait for the value of 5, then add it to the value of 10 in the cache

#             # Remove 5, get 0.
#                 # Set the value of 5 to be 1 in the cache
#             # Remove 1, get 4.
#                 # Wait for the value of 4, then add it to the value of 5 in the cache
cache = {0: 1}
def making_change(amount, denominations):
    global cache  # nonlocal cache
    if amount in cache:
        return cache[amount]
    cache[amount] = 0
    denominations.reverse()
    for i in range(len(denominations)):
        current_coin = denominations[i]
        new_amount = amount - current_coin
        if new_amount == 0:
            cache[amount] += 1
        elif new_amount > 0:
            cache[amount] += making_change(new_amount, denominations[i:])
    return cache[amount]

    # if amount == 0:
    #     return 1
    # count = 0
    # # Subtract each value in denoms in descending order

    # def recurse_helper(amount, denominations):
    #     nonlocal count
    #     for _ in range(len(denominations)):
    #         current_coin = denominations.pop()
    #         new_amount = amount - current_coin
    #         if new_amount == 0:
    #             count += 1
    #         elif new_amount > 0:
    #             denominations.append(current_coin)
    #             recurse_helper(new_amount, denominations)
    # recurse_helper(amount, denominations)
    # return count

    # If still > 0, subtract all values in desc
    # if == 0, add 1 to counter
    # if < 0, end


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    amount = 10
    denominations = [1, 5, 10, 25, 50]
    if len(sys.argv) > 1:
        amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(
        ways=making_change(amount, denominations), amount=amount))
