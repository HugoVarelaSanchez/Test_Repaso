import os, sys


#----SO----

#Funcion para saber el sistema operativo
def sistema_operativo():
    if os.name == 'nt':
        return 'cls'
    else:
        return 'clear'
        

    
#Funcion para limpiar pantalla
def limpiar_pantalla(sop):
    if sop == 'cls':
        os.system('cls')
    else:
        import termios
        os.system('clear')


def limpiar_buffer(sop):
    if sop=='cls':
        module = __import__('msvcrt')
        while module.kbhit():
                module.getch()
    
    else:
        module = __import__('termios')
        module.tcflush(sys.stdin, module.TCIFLUSH)


