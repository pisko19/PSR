# my_functions.py

class Complex:

    def __init__(self, r, i):
        """Inicializa um número complexo com a parte real e a parte imaginária."""
        self.r = r  # Armazena a parte real
        self.i = i  # Armazena a parte imaginária

    def add(self, y):
        """Soma outro número complexo ao atual."""
        self.r += y.r  # Adiciona a parte real do outro número
        self.i += y.i  # Adiciona a parte imaginária do outro número

    def multiply(self, y):
        """Multiplica outro número complexo pelo atual."""
        real_part = (self.r * y.r) - (self.i * y.i)  # (a*c - b*d)
        imag_part = (self.r * y.i) + (self.i * y.r)  # (a*d + b*c)
        self.r = real_part  # Atualiza a parte real
        self.i = imag_part  # Atualiza a parte imaginária

    def __str__(self):
        """Define o formato de impressão do número complexo."""
        if self.i >= 0:
            return f"{self.r} + {self.i}i"
        else:
            return f"{self.r} - {abs(self.i)}i"
