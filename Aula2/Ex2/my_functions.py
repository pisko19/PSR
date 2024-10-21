def divisors(value):
    """
    Return a list of dividers for the number value
    :param value: the number to test
    :return: a list of dividers.
    """
    divs = []
    for i in range(1, value + 1):
        if value % i == 0:
            divs.append(i)
    return divs


def isPrime(value):
    """
    Return a true or false
    :param value: the number to test
    :return: if its prime or not.
    """
    if value <= 1:
        return False
    for i in range(2, int(value**0.5) + 1):
        if value % i == 0:
            return False
    return True