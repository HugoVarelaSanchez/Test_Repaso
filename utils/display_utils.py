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

import time

from termcolor import colored
from utils.ascii_art_utils import escribir_palabra



#Funcion con prints de las presentaciones de las asignaturas
def impresiones_asignaturas(tipo=None, preguntas=None):
    if tipo == 'Menu_principal':
        escribir_palabra('Test Repaso')



# Funcion visual para cuando se saca calificacion perfecta
def nota_de_10(text, delay=0.1):
    rainbow_colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    
    for i, letter in enumerate(text):
        color = rainbow_colors[i % len(rainbow_colors)]
        print(colored(letter, color), end="", flush=True)
        time.sleep(delay)



#Temporal
def texto_preguntas(preguntas):
    print(f'''\nSi quieres contestar una pregunta introduce la respuesta [a b c d] en minusculas.
Si la quieres dejar en blanco, escriba s (skip).
      
De cuatas preguntas quieres el test? (20, 50, ..., {len(preguntas)})''')


