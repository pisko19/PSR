import time
import math
from colorama import Fore, Style, init
from my_functions import tic,toc

def main():
    current_time = time.ctime()  # Obtém a data e hora atual
    print(Fore.YELLOW + "Data e hora atual: " + Fore.CYAN + current_time)

    start_time = tic()
    print(Fore.GREEN + "\nIniciando o cálculo das raízes quadradas de 0 até 50 milhões...")

    for i in range(50_000_001):
        math.sqrt(i)

    elapsed_time = toc(start_time)

    print(Fore.YELLOW + f"\nO cálculo das raízes quadradas demorou: {Fore.RED}{elapsed_time:.2f} segundos.")

   

if __name__ == "__main__":
    main()
