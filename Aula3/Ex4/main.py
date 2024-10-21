from my_functions import Complex


def main():
    # Declara duas instâncias da classe Complex
    c1 = Complex(5, 3)  # 5 + 3i
    c2 = Complex(i=7, r=-2)  # -2 + 7i

    # Exibe o valor inicial de c1
    print("Inicial c1:", c1)  # Usa o método __str__
    
    

    # Soma c2 a c1
    c1.add(c2)
    print("Depois de somar c2 a c1:", c1)  # Usa o método __str__

    # Exibe o valor inicial de c2
    print("Inicial c2:", c2)  # Usa o método __str__
    
    # Multiplica c2 por c1
    c2.multiply(c1)
    print("Depois de multiplicar c2 por c1:", c2)  # Usa o método __str__

if __name__ == "__main__":
    main()
