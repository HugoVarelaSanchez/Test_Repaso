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

from colorama import Style, Fore
import time

from utils.test_selection import escoger_test, num_preguntas, obtener_respuesta
from utils.os_utils import limpiar_pantalla, limpiar_buffer, sistema_operativo
from utils.questions_utils import orden_aleatorio, mezclar_opciones
from utils.json_utils import get_items
from utils.Usuario import Usuario
from utils.display_utils import nota_de_10
from logger_config import logger


def test(asignatura, categoria, preguntas, sop, resp, traduccion, first_test=True):
        
        n =len(preguntas)
        falladas, nsnc = [], []

        if first_test:
            longitud_test = num_preguntas(int(len(preguntas)), asignatura, preguntas, sop)
            logger.info(f'Número de preguntas seleccionadas: {longitud_test}')
        else:
            longitud_test = len(preguntas)
            logger.info(f'Repetición de preguntas: {longitud_test} preguntas a responder.')
        
        orden = orden_aleatorio(preguntas)
        
        #Definimos al usuario
        jugador = Usuario(0, 0, 0)
        logger.info('Usuario inicializado')


        #Ahora va el bucle
        for i in range(1, longitud_test+1):

            limpiar_pantalla(sop)
            print(f'{jugador}\n')

            idx = orden[i-1]

            pregunta = mezclar_opciones(preguntas[str(idx)])
            print(f'{i}. {pregunta["q"]}\n')

            for u in range(0, len(pregunta["op"])):
                print(f'{resp[u]}.- {pregunta["op"][u]}')

            
            respuesta = obtener_respuesta(len(pregunta['op']), sop)


            # PREGUNTA SALTADA
            if respuesta == 's':

                
                jugador.no_contestadas += 1
                nsnc.append(i)
                logger.info(f"Pregunta {i} (ID {idx}): El usuario saltó la pregunta.")

                print(f'\n La respuesta correcta era: {pregunta["op"][pregunta["ok"]-1]}\n')

                if pregunta.get('jus'):
                    print(f'Justificacion: \n{pregunta["jus"]}')

                input('<Enter>')
                
                time.sleep(0.5)
            


            # PREGUNTA RESPONDIDA
            else:

                if traduccion[respuesta] == pregunta["ok"]:
                    jugador.acertadas += 1
                    print(f'\n{Fore.GREEN}¡Correcto!\n\n{Style.RESET_ALL}')
                    time.sleep(1)
                


                else:
                    jugador.falladas += 1
                    falladas.append(i)
                    logger.info(f"Pregunta {i} (ID {idx}): Respuesta incorrecta. Usuario eligió {respuesta}.")

                    print(f'\n{Fore.RED}¡Falso!\n\n{Style.RESET_ALL}La respuesta correcta era: {pregunta["op"][pregunta["ok"]-1]}\n')
                    
                    if pregunta.get('jus'):
                        print(f'Justificacion: \n{pregunta["jus"]}')
                    
                    input('<Enter>')


                    time.sleep(0.5)
        limpiar_pantalla(sop)



        # TEST COMPLETADO
        print(f'Has completado todas las preguntas:\n{jugador}')

        #Calculo de la nota
        nota = ((jugador.acertadas - jugador.falladas / 2) / longitud_test )*10
        nota = round(nota, 2)
        logger.info(f"Test finalizado. Resultado: {jugador.acertadas} AC, {jugador.falladas} FA, {jugador.no_contestadas} NC. Nota: {nota}")

        
        # Imprimir nota
        if nota <0:
            print(f'\nNota final: 0   ({nota})')
        else:
            print(f'\nNota final: {nota}\n\n')
        
        # NO FALLOS O NO CONTESTADAS

        if jugador.acertadas == longitud_test and first_test:
            nota_de_10('Hiciste un test perfecto!')
            time.sleep(1.5)
            # Aqui termina el test sin fallos

        # HAY FALLOS O NO CONTESTADAS
        else:

            limpiar_buffer(sop)
            if first_test:
                op_repe = input('¿Quieres repetir las falladas y no contestadas? (s)/n: ')

                if op_repe == 'n':
                    limpiar_pantalla(sop)
                    print(f'{Fore.RED}Reiniciando programa...{Style.RESET_ALL}')
                    time.sleep(0.5)
                    limpiar_pantalla(sop)
                    
                else:
                    indices_repetir = [orden[i-1] for i in (falladas + nsnc)]
                    preguntas_filtradas = {str(i): preguntas[str(orden[idx-1])] for i, idx in enumerate(indices_repetir, 1)}
                    
                    logger.info(f"Iniciando fase de repetición para {len(falladas) + len(nsnc)} preguntas.")
                    print('\nRepitiendo preguntas falladas y no contestadas:')
                    time.sleep(1.5)
                    test(asignatura, categoria, preguntas_filtradas, sop, resp, traduccion, first_test=False)
            
            limpiar_pantalla(sop)
            print(f'{Fore.RED}Reiniciando programa...{Style.RESET_ALL}')
            time.sleep(0.5)
            limpiar_pantalla(sop)




#----Main----     

def main():

    #Inicializamos variables:
    traduccion = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    resp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    asignatura = ''
    categoria = ''

    #Sistema operativo
    sop = sistema_operativo()
    logger.info(f'Sistema operativo detectado: {sop}')
    limpiar_pantalla(sop)


    while True:

        #Asignatura y preguntas de esa asignatura
        ruta_test, asignatura, categoria = escoger_test(sop, asignatura, categoria)
        logger.info(f"Test seleccionado: Asignatura='{asignatura}', Categoría='{categoria}', Ruta='{ruta_test}'")
        limpiar_pantalla(sop)

        preguntas = get_items(ruta_test)
        logger.info(f"Se cargaron {len(preguntas)} preguntas correctamente.")
        test(asignatura, categoria, preguntas, sop, resp, traduccion, first_test=True)


