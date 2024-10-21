import math
from colorama import Fore, Style, init
from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])

def addComplex(c1, c2):
    """
    Return the sum of two complex numbers
    :param: Complex number
    :param: Complex number
    :return: The sum of both complex numbers.
    """

    real_part = c1.r + c2.r
    im_part = c1.i + c2.i

    return Complex(real_part,im_part)


def multiplyComplex(x, y): 
    """
    Return the sum of two complex numbers
    :param: Complex number
    :param: Complex number
    :return: The sum of both complex numbers.
    """

    real_part = (x.r * y.r) - (x.i * y.i)  # Parte real: (a*c - b*d)
    imag_part = (x.r * y.i) + (x[1] * y.r)  # Parte imaginária: (a*d + b*c)
    
    return Complex(real_part, imag_part)  # Retorna o resultado como um número complexo (tuplo)

def printComplex(x):
    """Imprime um número complexo no formato a+bi."""
    real_part = x.r
    imag_part = x.i
    
    # Escolhe o sinal da parte imaginária
    if imag_part >= 0:
        print(Fore.GREEN +f"{real_part} + {imag_part}i")
    else:
        print(Fore.GREEN +f"{real_part} - {abs(imag_part)}i")  # Usa abs para remover o sinal extra

    




