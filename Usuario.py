from colorama import Fore, Style
class Usuario:
    def __init__(self, acertadas=0, falladas=0, no_contestadas=0):
        self.acertadas = acertadas
        self.falladas = falladas
        self.no_contestadas = no_contestadas

    def __repr__(self) -> str:
        return f'{Fore.GREEN}Aciertos: {self.acertadas}{Style.RESET_ALL}      {Fore.RED}Fallos: {self.falladas}{Style.RESET_ALL}      {Fore.LIGHTWHITE_EX}No contestadas: {self.no_contestadas}{Style.RESET_ALL}'
    def __str__(self) -> str:
        return f'{Fore.GREEN}Aciertos: {self.acertadas}{Style.RESET_ALL}      {Fore.RED}Fallos: {self.falladas}{Style.RESET_ALL}      {Fore.CYAN}No contestadas: {self.no_contestadas}{Style.RESET_ALL}'
