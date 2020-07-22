'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n):
    number_of_ways = 0

    def eat(total, to_eat):
        nonlocal number_of_ways
        total -= to_eat
        if total < 0:
            return
        elif total == 0:
            number_of_ways += 1
        else:
            eat(total, 1)
            if total >= 2:
                eat(total, 2)
            if total >= 3:
                eat(total, 3)

    if n <= 1:
        return 1
    else:
        eat(n, 0)
        return number_of_ways

    pass


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
