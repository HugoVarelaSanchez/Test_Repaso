from colorama import Style, Fore
def get_items(tipo):
    if tipo == 'icap':
        with open('archivos/preguntas.txt', 'r', encoding='utf-8') as archivo:
            cnt = archivo.readlines()
    elif tipo == 'medad':
         with open('archivos/medad_preguntas.txt', 'r', encoding='utf-8') as archivo:
            cnt = archivo.readlines()
    '''
    idea de como almacenar los items
    {numero de pregunta: [pregunta , {respuesta1:bool}, {respuesta2:bool}, {respuesta3:bool}, {respuesta4:bool}]}

    '''
    conv = {'a':1, 'b':2, 'c':3, 'd':4}
    preguntas = {}

    for i in range(0, len(cnt), 7):
        conjunto = cnt[i:i + 6]


        #                 num         pregunta            respuesta 1             respuesta 2                       respuesta 3             respuesta 4
        pregunta_nueva = [conjunto[0][3:], {conjunto[1][2:] : False}, {conjunto[2][2:] : False}, {conjunto[3][2:] : False}, {conjunto[4][2:] : False}]
        
        respuesta_correcta = conv[conjunto[5][0]]
        pregunta_nueva[respuesta_correcta] = {list(pregunta_nueva[respuesta_correcta].keys())[0]: True}


        preguntas[i//7+1] = pregunta_nueva
    
    return preguntas
    
class no_valid_response(Exception):
    pass

def obtener_respuesta():

    while True:

            try:
                eleccion = input('Respuesta: ')
                
                if (eleccion not in {'a', 'b', 'c', 'd', 's'}):
                    raise no_valid_response
                break

            except no_valid_response:
                print(f'\n{Fore.YELLOW}Escoja opcion [a b c d] en minusculas. Puede escojer [ s ] si quiere saltar la pregunta.{Style.RESET_ALL}\n')
    return eleccion


def num_preguntas(num_max:int):

    while True:

            try:
                eleccion = int(input('Total preguntas: '))
                
                if eleccion<1 or eleccion>num_max:
                    raise no_valid_response
                break


            except ValueError:
                print(f'\n{Fore.YELLOW}Debes introducir un numero entero.{Style.RESET_ALL}\n')
            except no_valid_response:
                print(f'\n{Fore.YELLOW}El minimo es 1 y el maximo es {num_max}.{Style.RESET_ALL}\n')
    return eleccion

