from colorama import Style, Fore
def get_items():

    with open('preguntas.txt', 'r', encoding='utf-8') as archivo:
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
        pregunta_nueva = [conjunto[0][3:], {conjunto[1][7:] : False}, {conjunto[2][7:] : False}, {conjunto[3][7:] : False}, {conjunto[4][7:] : False}]
        
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
