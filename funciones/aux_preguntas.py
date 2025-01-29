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


#Funcion para sacar las opciones disponibles.
#Idea a futuro es sacar las disponibles de un database
def asignaturas_disponibles():
    return os.listdir('asignaturas')
