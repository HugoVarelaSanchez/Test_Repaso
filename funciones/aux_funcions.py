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
from termcolor import colored
import os, time, sys, random, json

#Paquetes nuestros
from funciones.Usuario import Usuario
from funciones.os_functions import *
from funciones.aux_preguntas import *
from funciones.conversion_letras import *


#Excepcion
class no_valid_response(Exception):
    pass


#Temporal
def texto_preguntas(preguntas):
    print(f'''\nSi quieres contestar una pregunta introduce la respuesta [a b c d] en minusculas.
Si la quieres dejar en blanco, escriba s (skip).
      
De cuatas preguntas quieres el test? (20, 50, ..., {len(preguntas)})''')

#----Funciones seleccion----

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



#Funcion para que el usuario marque que asignatura quiere (implementar curses maybe)
def obtener_asignatura(lista_asignaturas_disponibles:list, sop):
    impresion = ''
    for i in lista_asignaturas_disponibles: impresion += i+' '
    while True:

            try:
                limpiar_pantalla(sop)
                impresiones_asignaturas(tipo='Menu_principal', preguntas=None)
                print(f'Asignaturas disponibles: {Fore.RED}{impresion}{Style.RESET_ALL}')
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

#print(f'\n{Fore.YELLOW}Las asignaturas disponibles son:\n{Fore.RED}impresion\n{Fore.YELLOW}Por favor escribala igual{Style.RESET_ALL}\n')


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
                print(f'\n{Fore.YELLOW}Por favor escriba tal cual la categoria disponible que quiera:\n{Fore.RED}{impresion}{Style.RESET_ALL}\n Si quiere retroceder escriba [ r ] ')
                time.sleep(2)
        
        return eleccion


    else:
        return False
    


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



#----Funciones impresion----


#Funcion con prints de las presentaciones de las asignaturas
def impresiones_asignaturas(tipo=None, preguntas=None):
    if tipo == 'medad':
        print(f'''╔════╗╔═══╗╔══╗╔════╗   ╔╗  ╔╗╔═══╗╔══╗ ╔══╗╔══╗ 
╚═╗╔═╝║╔══╝║╔═╝╚═╗╔═╝   ║║  ║║║╔══╝║╔╗╚╗║╔╗║║╔╗╚╗
  ║║  ║╚══╗║╚═╗  ║║     ║╚╗╔╝║║╚══╗║║╚╗║║╚╝║║║╚╗║
  ║║  ║╔══╝╚═╗║  ║║     ║╔╗╔╗║║╔══╝║║ ║║║╔╗║║║ ║║
  ║║  ║╚══╗╔═╝║  ║║     ║║╚╝║║║╚══╗║╚═╝║║║║║║╚═╝║
  ╚╝  ╚═══╝╚══╝  ╚╝     ╚╝  ╚╝╚═══╝╚═══╝╚╝╚╝╚═══╝


Si quieres contestar una pregunta introduce la respuesta [a b c d] en minusculas.
Si la quieres dejar en blanco, escriba s (skip).
Presione enter para pasar a la siguiente pregunta

Pronto añadire mas preguntas
Gracias por usar y mucho animo :)  
      
De cuatas preguntas quieres el test? (20, 50, ..., {len(preguntas)})

''')
    elif tipo == 'icap':
        print(f'''╔════╗╔═══╗╔══╗╔════╗   ╔══╗╔══╗╔══╗╔═══╗
╚═╗╔═╝║╔══╝║╔═╝╚═╗╔═╝   ╚╗╔╝║╔═╝║╔╗║║╔═╗║
  ║║  ║╚══╗║╚═╗  ║║      ║║ ║║  ║╚╝║║╚═╝║
  ║║  ║╔══╝╚═╗║  ║║      ║║ ║║  ║╔╗║║╔══╝
  ║║  ║╚══╗╔═╝║  ║║     ╔╝╚╗║╚═╗║║║║║║
  ╚╝  ╚═══╝╚══╝  ╚╝     ╚══╝╚══╝╚╝╚╝╚╝
      
Si quieres contestar una pregunta introduce la respuesta [a b c d] en minusculas.
Si la quieres dejar en blanco, escriba s (skip).

Pronto añadire mas preguntas
Gracias por usar y mucho animo :)  
      
De cuatas preguntas quieres el test? (20, 50, ..., {len(preguntas)})

''')
    elif tipo == 'Menu_principal':
        print(f'''╔════╗╔═══╗╔══╗╔════╗   ╔══╗╔═══╗╔═══╗
╚═╗╔═╝║╔══╝║╔═╝╚═╗╔═╝   ║╔╗║║╔═╗║║╔═╗║
  ║║  ║╚══╗║╚═╗  ║║     ║╚╝║║╚═╝║║╚═╝║
  ║║  ║╔══╝╚═╗║  ║║     ║╔╗║║╔══╝║╔══╝
  ║║  ║╚══╗╔═╝║  ║║     ║║║║║║   ║║   
  ╚╝  ╚═══╝╚══╝  ╚╝     ╚╝╚╝╚╝   ╚╝   


''')


# Funcion visual para cuando se saca calificacion perfecta
def nota_de_10(text, delay=0.1):
    rainbow_colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    for i, letter in enumerate(text):
        color = rainbow_colors[i % len(rainbow_colors)]
        print(colored(letter, color), end="", flush=True)
        time.sleep(delay)




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
            input('<Enter>')
            time.sleep(0.5)

        
        else:

            if traduccion[respuesta] == pregunta["ok"]:
                print(f'\n{Fore.GREEN}¡Correcto!\n\n{Style.RESET_ALL}')
                time.sleep(1)
            
            else:
                falladas.append(i)
                print(f'\n{Fore.RED}¡Falso!\n\n{Style.RESET_ALL}La respuesta correcta era: {pregunta["op"][pregunta["ok"]-1]}\n')
                input('<Enter>')
                time.sleep(0.5)
    
    limpiar_pantalla(sop)
    print(f'{Fore.RED}Has contestado todas las preguntas{Style.RESET_ALL}')
    time.sleep(1)



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
            



    
        