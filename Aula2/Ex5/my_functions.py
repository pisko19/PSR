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
    
    inputs = []  # Lista para armazenar todos os inputs
    inputs_other = {}  # Dicionário para armazenar inputs não numéricos

    while True:
        char = readchar.readchar()  # Lê um caractere
        
        # Verifica se o caractere lido é o caractere de parada
        if char == stop_char:
            print(f"Caractere de parada '{stop_char}' inserido.")
            break
        else:
            inputs.append(char)  # Adiciona o caractere à lista de inputs
            print(f"Caractere lido: {char}")

            # Adiciona o caractere não numérico ao dicionário
            if not char.isnumeric():
                order = len(inputs_other) + 1  # A ordem é o tamanho atual do dicionário + 1
                inputs_other[order] = char  # Armazena o caractere com a ordem como chave
                print(f"Caractere não numérico adicionado: {char}")

    # Cria a lista de números usando list comprehension
    inputs_numeric = [char for char in inputs if char.isnumeric()]

    # Exibe a contagem de números e não-números
    total_numbers = len(inputs_numeric)
    total_others = len(inputs) - total_numbers

    # Ordena a lista de números em ordem crescente
    sorted_numeric = sorted(inputs_numeric)

    print('Você digitou ' + str(total_numbers) + ' números.')
    print('Você digitou ' + str(total_others) + ' outros.')

    # Imprime a lista de números ordenados
    print('Números inseridos em ordem crescente:', sorted_numeric)

    # Imprime o dicionário de outros
    print('Inputs não numéricos:', inputs_other)

def main():
    print("Por favor, insira um caractere:")
    # printAllPreviousChars() # Supondo que você queira usar isso, adicione conforme necessário
    
    print("\nAgora vamos ler caracteres até encontrar o caractere 'X':")
    countNumbersUpto('X')

if __name__ == "__main__":
    main()



