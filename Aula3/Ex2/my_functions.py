import math
from colorama import Fore, Style, init


def addComplex(c1, c2):
    """
    Return the sum of two complex numbers
    :param: Complex number
    :param: Complex number
    :return: The sum of both complex numbers.
    """

    real_part = c1[0] + c2[0]
    im_part = c1[1] + c2[1]

    return (real_part,im_part)


def multiplyComplex(x, y): 
    """
    Return the sum of two complex numbers
    :param: Complex number
    :param: Complex number
    :return: The sum of both complex numbers.
    """

    real_part = (x[0] * y[0]) - (x[1] * y[1])  # Parte real: (a*c - b*d)
    imag_part = (x[0] * y[1]) + (x[1] * y[0])  # Parte imaginária: (a*d + b*c)
    
    return (real_part, imag_part)  # Retorna o resultado como um número complexo (tuplo)

def printComplex(x):
    """Imprime um número complexo no formato a+bi."""
    real_part = x[0]
    imag_part = x[1]
    
    # Escolhe o sinal da parte imaginária
    if imag_part >= 0:
        print(Fore.GREEN +f"{real_part} + {imag_part}i")
    else:
        print(Fore.GREEN +f"{real_part} - {abs(imag_part)}i")  # Usa abs para remover o sinal extra

    




