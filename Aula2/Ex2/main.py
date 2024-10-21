#!/usr/bin/env python3
from colorama import Fore, Style, init
from my_functions import divisors,isPrime

maximum_number = 50

def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))

    for i in range(2, maximum_number):  # Começar de 2, porque 0 e 1 não são primos
        if isPrime(i):
            print(Fore.GREEN + 'Number ' + str(i) + ' is prime.' + Style.RESET_ALL)
        else:
            print('Number ' + str(i) + ' is not prime. Divisors: ' + str(divisors(i)))

if __name__ == "__main__":
    main()