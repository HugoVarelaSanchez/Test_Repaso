#
# Copyright (C) 2025 Hugo Varela Sanchez (HugoVarelaSanchez)
# 
# Este archivo es parte de Test_Repaso
# GitHub: https://github.com/HugoVarelaSanchez/Test_Repaso
# 
# Test_Repaso es software libre: puedes redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU versión 3
# publicada por la Free Software Foundation.
# 
# Test_Repaso se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; sin siquiera la garantía implícita de
# COMERCIABILIDAD o IDONEIDAD PARA UN PROPÓSITO PARTICULAR. Consulta
# la Licencia Pública General GNU para más detalles.
# 
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con Test_Repaso. Si no es así, consulta <https://www.gnu.org/licenses/>.
#

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
