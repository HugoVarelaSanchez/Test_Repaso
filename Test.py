from archivos.aux_funcions import get_items, obtener_respuesta, num_preguntas
from archivos.Usuario import Usuario
import random
import sys
from colorama import Style, Fore

#Obtenemos las preguntas y el usuario
preguntas = get_items()
jugador = Usuario(0, 0, 0)

#Inicializamos variables
n =len(preguntas)
falladas = []
nsnc = []

#Añadir texto explicando como furula, usar s basicamente
print(f'''
╔════╗╔═══╗╔══╗╔════╗   ╔══╗╔══╗╔══╗╔═══╗
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
longitud_test = num_preguntas(int(len(preguntas)))

orden = []
for i in range(1, len(preguntas)+1):
    orden.append(i)

orden = random.sample(orden, len(orden))


for i in range(1, longitud_test+1):


    print(f'\n---------------------------------------------------------\n')
    #Imprimimos aciertos, fallos, skipped
    print(f'{jugador}\n')

    #Escojemos orden aleatorio de respuestas
    valores = random.sample([1, 2, 3, 4], 4)
    a , b, c, d = valores
    conv2 = {'a':a, 'b':b, 'c':c, 'd':d}

    #Escojemos orden de preguntas aleatorias, si ya se pregunto, 
    #vuelve a calcular hasta que se encuentre una que no se pregunto
    #Y la almacena en las ya guardadas
    
    eleccion_pregunta = orden[i-1]


    #Cojemos eleccion pregunta -1 porque va de 1 a 50
    actual = preguntas[eleccion_pregunta]
    

    #Imprimimos pregunta y respuestas
    print(f'''{i}. {actual[0]}
\ta.- {list(actual[a].keys())[0]}\tb.- {list(actual[b].keys())[0]}\tc.- {list(actual[c].keys())[0]}\td.- {list(actual[d].keys())[0]}\n''')
    
    for u in range(1, 5):
        if list(actual[u].values())[0] == True:
            respuesta_correcta = list(actual[u].keys())[0].strip()
    


    #Obtenemos respuesta y comprobamos si esta bien o mal
    respuesta = obtener_respuesta()

    if respuesta == 's':
        jugador.no_contestadas += 1
        nsnc.append(i)
        print(f'\n La respuesta correcta era: {respuesta_correcta}\n')

    else:
        if list(actual[conv2[respuesta]].values())[0] == True:
            jugador.acertadas += 1
            print(f'\n{Fore.GREEN}¡Correcto!\n\n{Style.RESET_ALL}')
        else:
            jugador.falladas += 1
            falladas.append(i)
            print(f'\n{Fore.RED}¡Falso!{Style.RESET_ALL}\n La respuesta correcta era: {respuesta_correcta}\n')
    




#Una vez todas las preguntas se han preguntado, se termina
print(f'\n---------------------------------------------------------\n')

print(f'\n\nHas completado todas las preguntas:')
print(jugador)


#Calcular aqui la nota final
nota = (  (jugador.acertadas - jugador.falladas / 2) / longitud_test )*10
nota = round(nota, 2)

if nota <0:
    print(f'\nNota final: 0   ({nota})')
else:
    print(f'\nNota final: {nota}\n\n')


if len(falladas) > 1:
    print(f'\nFallaste las preguntas numero:', *falladas)
elif len(falladas)>0:
    print(f'\nFallaste la pregunta numero:', *falladas)

if len(nsnc)>1:
    print(f'\nNo contestaste las preguntas numero:', *nsnc)
elif len(nsnc)>0:
    print(f'\nNo contestaste la pregunta numero:', *nsnc)

if jugador.acertadas == longitud_test:
    print(f'{Fore.MAGENTA}Hiciste un test perfecto!{Style.RESET_ALL}')

