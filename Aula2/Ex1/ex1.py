#!/usr/bin/env python3
# --------------------------------------------------
# A simple python script to check perfect numbers
# Eurico Pedrosa.
# PSR, September 2024.
# --------------------------------------------------

maximum_number = 100    # maximum number to test


def divisors(value):
    """
    Return a list of dividers for the number value
    :param value: the number to test
    :return: a list of dividers.
    """
    divs = []
    for i in range(1, value):  # Excluir o próprio número (range até value, não value+1)
        if value % i == 0:
            divs.append(i)
    return divs

def isPerfect(value):
    """ Verifica se a soma dos divisores (exceto o próprio número) é igual ao número. """
    divs = divisors(value)
    return sum(divs) == value

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):  # Começar em 1, já que 0 não faz sentido para números perfeitos
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')

if __name__ == "__main__":
    main()
