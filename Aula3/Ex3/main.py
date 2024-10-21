from my_functions import addComplex, multiplyComplex,printComplex
from collections import namedtuple


Complex = namedtuple('Complex', ['r', 'i'])

def main():
    c1 = Complex(5,3)
    c2 = Complex(i=2,r=-1)

    printComplex(addComplex(c1,c2))
    printComplex(multiplyComplex(c1,c2))

if __name__ == "__main__":
    main()
