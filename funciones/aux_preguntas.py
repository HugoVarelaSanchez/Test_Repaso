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

import random, os, json

#Funcion para obtener las preguntas
def get_items(ruta):
    
    with open(ruta, 'r', encoding='utf-8') as archivo:
        cnt = json.load(archivo)
    
    
    return cnt
    
#Funcion para ordenar aleatoriamente las preguntas
def orden_aleatorio(preguntas):
    orden = []
    for i in range(1, len(preguntas)+1):
        orden.append(i)

    orden = random.sample(orden, len(orden))
    return orden


def mezclar_opciones(pregunta):
    opciones = pregunta['op'].copy()
    correcta = opciones[pregunta['ok']-1]

    random.shuffle(opciones)

    nueva_correcta = opciones.index(correcta) + 1

    return {'q': pregunta['q'],
            'op': opciones,
            'ok': nueva_correcta,
            'jus': pregunta.get('jus', '') # Campo opcional, las preguntas pueden tener una justificacion
            }



#Funcion para sacar las opciones disponibles.
#Idea a futuro es sacar las disponibles de un database
def asignaturas_disponibles():
    return os.listdir('asignaturas')
