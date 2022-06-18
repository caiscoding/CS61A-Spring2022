def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"
    if num < 10:
        if num == prev_digit:
            return 1
        else:
            return 0
    lastDigit = num % 10
    currDigit = num // 10
    return int(lastDigit == prev_digit or lastDigit == currDigit % 10) + neighbor_digits(currDigit, lastDigit)
