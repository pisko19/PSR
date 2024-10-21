import readchar

def printAllPreviousChars():
    """
    Reads char from keyboard
    """
    # Ler um caractere do usuário
    char = readchar.readchar()
    
    # Converter o caractere em seu valor ASCII
    char_code = ord(char)
    
    # Iterar e imprimir todos os caracteres desde ' ' (espaço, ASCII 32) até o caractere lido
    for i in range(32, char_code + 1):
        print(chr(i), end=' ')
    
    print()  # Apenas para adicionar uma nova linha após imprimir todos os caracteres

def readAllUpTo(stop_char):
    print(f"Digite caracteres. O programa parará quando o caractere '{stop_char}' for inserido.")
    
    while True:
        char = readchar.readchar()  # Lê um caractere
        
        # Verifica se o caractere lido é o caractere de parada
        if char == stop_char:
            print(f"Caractere de parada '{stop_char}' inserido. Terminando a leitura.")
            break
        else:
            print(f"Caractere lido: {char}")

def countNumbersUpto(stop_char='X'):
    print(f"Digite caracteres. O programa parará quando o caractere '{stop_char}' for inserido.")
    
    digit_count = 0
    non_digit_count = 0
    
    while True:
        char = readchar.readchar()  # Lê um caractere
        
        # Verifica se o caractere lido é o caractere de parada
        if char == stop_char:
            print(f"Caractere de parada '{stop_char}' inserido.")
            break
        else:
            # Verifica se o caractere é um número
            if char.isnumeric():
                digit_count += 1
            else:
                non_digit_count += 1
            
            print(f"Caractere lido: {char}")

    # Exibe a contagem de algarismos e não algarismos
    print(f"Números: {digit_count}, Não Números: {non_digit_count}")
