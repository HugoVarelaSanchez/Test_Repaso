from colorama import Style, Fore
from termcolor import colored
from funciones.Usuario import Usuario
import os, time, sys, random, json



#Excepcion
class no_valid_response(Exception):
    pass

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
        os.system('clear')


#----Preguntas---


#Funcion para obtener las preguntas
def get_items(tipo):
    if tipo == 'icap':
        with open('preguntas/icap.json', 'r', encoding='utf-8') as archivo:
            cnt = json.load(archivo)
    elif tipo == 'medad':
         with open('preguntas/medad.json', 'r', encoding='utf-8') as archivo:
            cnt = json.load(archivo)
    
    return cnt
    
#Funcion para ordenar aleatoriamente las preguntas
def orden_aleatorio(preguntas):
    orden = []
    for i in range(1, len(preguntas)+1):
        orden.append(i)

    orden = random.sample(orden, len(orden))
    return orden


#Funcion para sacar las opciones disponibles.
#Idea a futuro es sacar las disponibles de un database
def asignaturas_disponibles():
    return {'icap', 'medad'}


#----Funciones seleccion----


#Funcion para elegir la respuesta
def obtener_respuesta(num):

    while True:
            opciones = ['s', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
            try:
                eleccion = input('\nRespuesta: ')
                
                if (eleccion not in opciones[0:(num+1)]):
                    raise no_valid_response
                break

            except no_valid_response:
                print(f'\n{Fore.YELLOW}Escoja opcion (', *opciones[1:(num+1)],f') en minusculas. Puede escojer [ s ] si quiere saltar la pregunta.{Style.RESET_ALL}\n')
    return eleccion

#Funcion para elegir el numero de preguntas
def num_preguntas(num_max:int, tipo, preguntas, sop):

    while True:

            try:
                limpiar_pantalla(sop)
                impresiones_asignaturas(tipo=tipo, preguntas=preguntas)
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
def obtener_asignatura(lista_asignaturas_disponibles:set, sop):
    impresion = ''
    for i in lista_asignaturas_disponibles: impresion += i+' '
    while True:

            try:
                limpiar_pantalla(sop)
                impresiones_asignaturas(tipo='Menu_principal', preguntas=None, impresion=impresion)
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




#----Funciones impresion----


#Funcion con prints de las presentaciones de las asignaturas
def impresiones_asignaturas(tipo=None, preguntas=None, impresion=None):
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

Asignaturas disponibles: {Fore.RED}{impresion}{Style.RESET_ALL}
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

        pregunta = preguntas[str(idx)]
        print(f'{i}. {pregunta["q"]}\n')

        for u in range(0, len(pregunta["op"])):
            print(f'{resp[u]}.- {pregunta["op"][u]}')
        
        
        respuesta = obtener_respuesta(len(pregunta['op']))

        if respuesta == 's':
            print(f'\n La respuesta correcta era: {pregunta["op"][pregunta["ok"]-1]}\n')
            input('<Enter>')
        
        else:

            if traduccion[respuesta] == pregunta["ok"]:
                print(f'\n{Fore.GREEN}¡Correcto!\n\n{Style.RESET_ALL}')
                time.sleep(1)
            
            else:
                falladas.append(i)
                print(f'\n{Fore.RED}¡Falso!\n\n{Style.RESET_ALL}La respuesta correcta era: {pregunta["op"][pregunta["ok"]-1]}\n')
                input('<Enter>')
    
    limpiar_pantalla(sop)
    print(f'{Fore.RED}Has contestado todas las preguntas{Style.RESET_ALL}')
    time.sleep(1)



#----Main----     

def main():

    #Inicializamos variables:
    traduccion = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    resp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    #Definimos al usuario
    jugador = Usuario(0, 0, 0)

    #Sistema operativo
    sop = sistema_operativo()
    limpiar_pantalla(sop)

    #Asignatura y preguntas de esa asignatura
    asignatura = obtener_asignatura(asignaturas_disponibles(), sop)
    limpiar_pantalla(sop)
    preguntas = get_items(asignatura)
    n =len(preguntas)
    falladas, nsnc = [], []

    #Obtenemos el numero de preguntas y el orden
    
    longitud_test = num_preguntas(int(len(preguntas)), asignatura, preguntas, sop)
    orden = orden_aleatorio(preguntas)

    

    #Ahora va el bucle
    for i in range(1, longitud_test+1):
        limpiar_pantalla(sop)
        print(f'{jugador}\n')

        idx = orden[i-1]

        pregunta = preguntas[str(idx)]
        print(f'{i}. {pregunta["q"]}\n')

        for u in range(0, len(pregunta["op"])):
            print(f'{resp[u]}.- {pregunta["op"][u]}')
        
        
        respuesta = obtener_respuesta(len(pregunta['op']))

        if respuesta == 's':
            jugador.no_contestadas += 1
            nsnc.append(i)
            print(f'\n La respuesta correcta era: {pregunta["op"][pregunta["ok"]-1]}\n')
            input('<Enter>')
        
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
        op_repe = input('¿Quieres repetir las falladas y no contestadas? (s)/n: ')
        if op_repe == 'n':
            limpiar_pantalla(sop)
            print(f'{Fore.RED}Reiniciando programa...{Style.RESET_ALL}')
            time.sleep(0.5)
            limpiar_pantalla(sop)
            #sys.exit()
        else:
            repetir(falladas, nsnc, orden, sop, preguntas, resp, traduccion)
        



    
        