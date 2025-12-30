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

import os, time, sys

from colorama import Style, Fore
from utils.os_utils import limpiar_pantalla, limpiar_buffer
from utils.questions_utils import asignaturas_disponibles
from utils.ascii_art_utils import escribir_palabra
from utils.display_utils import impresiones_asignaturas, texto_preguntas
from utils.exceptions_utils import no_valid_response


    #?=====================================================
    #?                    Asignatura                    
    #?=====================================================


def obtener_asignatura(lista_asignaturas_disponibles:list, sop):
    impresion = ''
    for i in lista_asignaturas_disponibles: impresion += i+' '
    
    while True:
            try:
                limpiar_pantalla(sop)
                impresiones_asignaturas(tipo='Menu_principal', preguntas=None)
                print(f'\n\n\nAsignaturas disponibles: {Fore.RED}{impresion}{Style.RESET_ALL}')
                limpiar_buffer(sop)

                eleccion = (input('\n¿De que asignatura desea los tests?: '))
                
                if (eleccion not in lista_asignaturas_disponibles):
                    raise no_valid_response
                break


            except ValueError:
                print(f'\n\n{Fore.YELLOW}Debes introducir una asignatura valida.{Style.RESET_ALL}\n')
                time.sleep(2)

            except no_valid_response:
                print(f'\n{Fore.YELLOW}Por favor escriba tal cual la asignatura disponible que quiera:\n{Fore.RED}{impresion}{Style.RESET_ALL}')
                time.sleep(2)
    return eleccion


    #?=====================================================
    #?                    Categoria                    
    #?=====================================================

    

def elegir_categoria(asignatura, sop):

    categorias = os.listdir(f'asignaturas/{asignatura}')

    if len(categorias)>0:
        opciones = categorias.copy()
        opciones.append('r')
        impresion = ''
        for i in categorias: impresion += i+' '

        while True:

            try:
                limpiar_pantalla(sop)
                escribir_palabra(f'test {asignatura}')
                print(f'\n\n\nCategorias disponibles para {asignatura}: {Fore.RED}{impresion}{Style.RESET_ALL}')
                limpiar_buffer(sop)

                eleccion = (input('\n¿De que categoria desea los tests?: '))
                
                if (eleccion not in opciones):
                    raise no_valid_response
                break


            except ValueError:
                print(f'\n\n{Fore.YELLOW}Debes introducir una categoria valida.{Style.RESET_ALL}\n')
                time.sleep(2)

            except no_valid_response:
                print(f'\n{Fore.YELLOW}Por favor escriba tal cual la categoria disponible que quiera:\n{Fore.RED}{impresion}{Style.RESET_ALL}\n\nSi quiere retroceder escriba [ r ] ')
                time.sleep(2)
        
        return eleccion


    else:
        return False
    



    #?=====================================================
    #?                  Escoger Test                    
    #?=====================================================



def escoger_test(sop, asignatura, categoria):
    
    while True:

        if(len(os.listdir(f'asignaturas'))<1):
            limpiar_pantalla(sop)
            print(f'{Fore.RED}No hay ninguna informacion{Style.RESET_ALL}')
            time.sleep(1.5)
            sys.exit()
        

        elif asignatura == '':
            categoria = ''
            asignatura = obtener_asignatura(asignaturas_disponibles(), sop)
        

        while True:  
            
            if (len(os.listdir(f'asignaturas/{asignatura}'))<1):
                
                print(f'\nDe momento no hay informacion')
                time.sleep(1.5)

                asignatura = ''
                break

            elif (categoria == ''):  
                categoria = elegir_categoria(asignatura, sop)

            if categoria == 'r':
                asignatura = ''
                break


            while True:
                if len(os.listdir(f'asignaturas/{asignatura}/{categoria}'))>0:
                    test = elegir_test(asignatura, categoria, sop)
                else:
                    #test = os.listdir(f'asignaturas/{asignatura}/{categoria}')[0]
                    print(f'\nDe momento no hay test')
                    time.sleep(2)
                    categoria=''
                    break
                
                
                if test == 'r':
                    categoria=''
                    break
                
                else:
                    ruta_test = f'asignaturas/{asignatura}/{categoria}/{test}.json'
                    return ruta_test, asignatura, categoria


    return None




def elegir_test(asignatura, categoria, sop):
    traduccion = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    inverso = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    opciones = [os.path.splitext(f)[0] for f in os.listdir(f'asignaturas/{asignatura}/{categoria}') if f.endswith(".json")]
    limpiar_pantalla(sop)
    escribir_palabra(f'test {asignatura}')
    print(f'\n\n')
    print("\n".join(f"{inverso[i]}.- {nombre}" for i, nombre in enumerate(opciones)))

    
    while True:
                letras = ['r', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
                try:
                    limpiar_buffer(sop)
                    limpiar_buffer(sop)

                    eleccion = input('\nRespuesta: ')
                    
                    if (eleccion not in letras[0:(len(opciones)+1)]):
                        raise no_valid_response
                    break

                except no_valid_response:
                    print(f'\n{Fore.YELLOW}Escoja la opcion que quiera en minusculas. \nPuede escoger [ r ] si quiere retroceder.{Style.RESET_ALL}\n')
    
    if eleccion == 'r':
        return eleccion
    else:
        
        test = opciones[traduccion[eleccion]-1]
        return test
    return 







    #?=====================================================
    #?          Numero de preguntas por test                    
    #?=====================================================

#Funcion para elegir el numero de preguntas
def num_preguntas(num_max:int, asignatura, preguntas, sop):

    while True:

            try:
                limpiar_pantalla(sop)
                escribir_palabra(f'test {asignatura}')
                texto_preguntas(preguntas)
                limpiar_buffer(sop)
                eleccion = int(input('Total preguntas: '))
                
                if eleccion<1 or eleccion>num_max:
                    raise no_valid_response
                break


            except ValueError:
                print(f'\n{Fore.YELLOW}Debes introducir un numero entero.{Style.RESET_ALL}\n')
                time.sleep(1)
            except no_valid_response:
                print(f'\n{Fore.YELLOW}El minimo es 1 y el maximo es {num_max}.{Style.RESET_ALL}\n')
                time.sleep(1)
    return eleccion


    #?=====================================================
    #?              Eleccion opcion                    
    #?=====================================================

#Funcion para elegir la respuesta
def obtener_respuesta(num, sop):

    while True:
            opciones = ['s', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
            try:
                limpiar_buffer(sop)
                limpiar_buffer(sop)
                eleccion = input('\nRespuesta: ')
                
                if (eleccion not in opciones[0:(num+1)]):
                    raise no_valid_response
                break

            except no_valid_response:
                print(f'\n{Fore.YELLOW}Escoja opcion (', *opciones[1:(num+1)],f') en minusculas. Puede escojer [ s ] si quiere saltar la pregunta.{Style.RESET_ALL}\n')
    return eleccion


