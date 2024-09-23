#!/usr/bin/env python3

from colorama import Fore, Style, init

def divisors(value):
    """ Retorna os divisores de um número que não é primo. """
    divs = []
    for i in range(1, value + 1):
        if value % i == 0:
            divs.append(i)
    return divs

maximum_number = 50

def isPrime(value):
    if value <= 1:
        return False
    for i in range(2, int(value**0.5) + 1):
        if value % i == 0:
            return False
    return True

def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))

    for i in range(2, maximum_number):  # Começar de 2, porque 0 e 1 não são primos
        if isPrime(i):
            print(Fore.GREEN + 'Number ' + str(i) + ' is prime.' + Style.RESET_ALL)
        else:
            print('Number ' + str(i) + ' is not prime. Divisors: ' + str(divisors(i)))

if __name__ == "__main__":
    main()
