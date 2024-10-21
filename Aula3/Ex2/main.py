import time
import math
from colorama import Fore, Style, init
from my_functions import addComplex, multiplyComplex,printComplex

def main():
    c1 = (5,3)
    c2 = (-2,7)

    printComplex(addComplex(c1,c2))
    printComplex(multiplyComplex(c1,c2))

if __name__ == "__main__":
    main()
