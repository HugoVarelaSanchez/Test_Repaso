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

import random, os

    
def orden_aleatorio(preguntas):
    '''Funcion para devolver un orden aleatorio de preguntas'''
    orden = []
    for i in range(1, len(preguntas)+1):
        orden.append(i)

    orden = random.sample(orden, len(orden))
    return orden


def mezclar_opciones(pregunta):
    '''Funcion para mezclar las opciones de una pregunta'''
    opciones = pregunta['op'].copy()
    correcta = opciones[pregunta['ok']-1]

    random.shuffle(opciones)

    nueva_correcta = opciones.index(correcta) + 1

    return {'q': pregunta['q'],
            'op': opciones,
            'ok': nueva_correcta,
            'jus': pregunta.get('jus', '') # Campo opcional, las preguntas pueden tener una justificacion
            }


def asignaturas_disponibles():
    '''Funcion para obtener las asignaturas disponibles'''
    return os.listdir('asignaturas')
