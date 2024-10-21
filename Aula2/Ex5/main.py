#!/usr/bin/env python3

import argparse
from colorama import Fore, Style, init
from my_functions import printAllPreviousChars, readAllUpTo,countNumbersUpto

def main():
 
   print("\nAgora vamos ler caracteres até encontrar o caractere 'X':")
   countNumbersUpto('X')

if __name__ == "__main__":
    main()
