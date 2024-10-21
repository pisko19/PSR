#!/usr/bin/env python3

import argparse
from colorama import Fore, Style, init
from my_functions import divisors, isPrime

def main():
    # Configuração do argparse para lidar com argumentos da linha de comando
    parser = argparse.ArgumentParser(description='Calcular números primos até um valor máximo.')
    parser.add_argument('--max_number', type=int, default=100, help='O valor máximo até o qual serão calculados os números primos')

    # Parseia os argumentos
    args = parser.parse_args()

    maximum_number = args.max_number

    print("Starting to compute prime numbers up to " + str(maximum_number))

    for i in range(2, maximum_number + 1):  # Começar de 2, porque 0 e 1 não são primos
        if isPrime(i):
            print(Fore.GREEN + 'Number ' + str(i) + ' is prime.' + Style.RESET_ALL)
        else:
            print('Number ' + str(i) + ' is not prime. Divisors: ' + str(divisors(i)))

if __name__ == "__main__":
    main()
