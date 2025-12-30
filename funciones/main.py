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

from funciones.aux_funcions import escoger_test, num_preguntas, obtener_respuesta
from funciones.os_functions import limpiar_pantalla, limpiar_buffer, sistema_operativo
from funciones.aux_preguntas import get_items, orden_aleatorio, mezclar_opciones
from funciones.Usuario import Usuario
from funciones.visualizar import nota_de_10


#----Repeticion----

def repetir(falladas, nsns, orden, sop, preguntas, resp, traduccion):
    limpiar_pantalla(sop)
    print('Repitiendo preguntas falladas y no contestadas:')
    time.sleep(1.5)

    lista_completa = falladas+nsns

    for i in lista_completa:
        limpiar_pantalla(sop)

        idx = orden[i-1]

        pregunta = mezclar_opciones(preguntas[str(idx)])
        print(f'{i}. {pregunta["q"]}\n')

        for u in range(0, len(pregunta["op"])):
            print(f'{resp[u]}.- {pregunta["op"][u]}')
        
        
        respuesta = obtener_respuesta(len(pregunta['op']), sop)

        if respuesta == 's':
            print(f'\n La respuesta correcta era: {pregunta["op"][pregunta["ok"]-1]}\n')
            if pregunta.get('jus'):
                print(f'Justificacion: \n{pregunta["jus"]}\n\n')
            input('<Enter>')
            time.sleep(0.5)

        
        else:

            if traduccion[respuesta] == pregunta["ok"]:
                print(f'\n{Fore.GREEN}¡Correcto!\n\n{Style.RESET_ALL}')
                time.sleep(1)
            
            else:
                falladas.append(i)
                print(f'\n{Fore.RED}¡Falso!\n\n{Style.RESET_ALL}La respuesta correcta era: {pregunta["op"][pregunta["ok"]-1]}\n')
                if pregunta.get('jus'):
                    print(f'Justificacion: \n{pregunta["jus"]}')
                input('<Enter>')
                time.sleep(0.5)
    
    limpiar_pantalla(sop)
    print(f'{Fore.RED}Has contestado todas las preguntas{Style.RESET_ALL}')
    time.sleep(1)



#----Main----     

def main():

    #Inicializamos variables:
    traduccion = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    resp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    asignatura = ''
    categoria = ''

    #Sistema operativo
    sop = sistema_operativo()
    limpiar_pantalla(sop)


    while True:

        

        #Asignatura y preguntas de esa asignatura
        ruta_test, asignatura, categoria = escoger_test(sop, asignatura, categoria)
        limpiar_pantalla(sop)

        preguntas = get_items(ruta_test)
        n =len(preguntas)

        falladas, nsnc = [], []


        #Obtenemos el numero de preguntas y el orden 
        longitud_test = num_preguntas(int(len(preguntas)), asignatura, preguntas, sop)
        orden = orden_aleatorio(preguntas)

        
        #Definimos al usuario
        jugador = Usuario(0, 0, 0)


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

            if respuesta == 's':
                jugador.no_contestadas += 1
                nsnc.append(i)
                print(f'\n La respuesta correcta era: {pregunta["op"][pregunta["ok"]-1]}\n')

                if pregunta.get('jus'):
                    print(f'Justificacion: \n{pregunta["jus"]}')

                input('<Enter>')
                time.sleep(0.5)
            
            else:

                if traduccion[respuesta] == pregunta["ok"]:
                    jugador.acertadas += 1
                    print(f'\n{Fore.GREEN}¡Correcto!\n\n{Style.RESET_ALL}')
                    time.sleep(1)
                
                else:
                    jugador.falladas += 1
                    falladas.append(i)
                    print(f'\n{Fore.RED}¡Falso!\n\n{Style.RESET_ALL}La respuesta correcta era: {pregunta["op"][pregunta["ok"]-1]}\n')
                    if pregunta.get('jus'):
                        print(f'Justificacion: \n{pregunta["jus"]}')
                    input('<Enter>')
                    time.sleep(0.5)


        limpiar_pantalla(sop)
        print(f'Has completado todas las preguntas:\n{jugador}')

        #Calculo de la nota
        nota = (  (jugador.acertadas - jugador.falladas / 2) / longitud_test )*10
        nota = round(nota, 2)
        
        if nota <0:
            print(f'\nNota final: 0   ({nota})')
        else:
            print(f'\nNota final: {nota}\n\n')
        
        if jugador.acertadas == longitud_test:
            nota_de_10('Hiciste un test perfecto!')
            time.sleep(1.5)
        else:
            limpiar_buffer(sop)
            op_repe = input('¿Quieres repetir las falladas y no contestadas? (s)/n: ')
            if op_repe == 'n':
                limpiar_pantalla(sop)
                print(f'{Fore.RED}Reiniciando programa...{Style.RESET_ALL}')
                time.sleep(0.5)
                limpiar_pantalla(sop)
                #sys.exit()
            else:
                repetir(falladas, nsnc, orden, sop, preguntas, resp, traduccion)
            



    
        