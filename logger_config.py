import logging
import sys
import os
from colorama import Fore, Style, init

# Crear directorio de logs si no existe
if not os.path.exists('logs'):
    os.makedirs('logs')

class ColorFormatter(logging.Formatter):
    '''Formateador de logs con colores para la consola.'''
    COLORS = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
    }

    def format(self, record):
        color = self.COLORS.get(record.levelno, Fore.WHITE)
        fmt = f"%(asctime)s {color}%(levelname)-8s{Style.RESET_ALL} [%(filename)s:%(lineno)d] {color}%(message)s{Style.RESET_ALL}"
        formatter = logging.Formatter(fmt, datefmt='%H:%M:%S')
        return formatter.format(record)

# Configuración 
logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)

# Archivo
file_handler = logging.FileHandler('logs/main_logs.txt')
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', '%d-%m-%Y %H:%M:%S'))
logger.addHandler(file_handler)

# Consola
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(ColorFormatter())
logger.addHandler(console_handler)
console_handler.setLevel(logging.WARNING) 
logger.addHandler(console_handler)