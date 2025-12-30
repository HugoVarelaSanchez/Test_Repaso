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

import os, sys


def sistema_operativo():
    '''Funcion para saber el sistema operativo'''
    if os.name == 'nt':
        return 'cls'
    else:
        return 'clear'
        
    
def limpiar_pantalla(sop):
    '''Funcion para limpiar la pantalla segun el sistema operativo'''
    if sop == 'cls':
        os.system('cls')
    else:
        import termios
        os.system('clear')


def limpiar_buffer(sop):
    '''Funcion para limpiar el buffer de entrada segun el sistema operativo'''

    if sop=='cls':
        module = __import__('msvcrt')
        while module.kbhit():
                module.getch()
    
    else:
        module = __import__('termios')
        module.tcflush(sys.stdin, module.TCIFLUSH)