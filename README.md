# Test Teoria
Programa con test de repaso 

Preguntas aleatorias con respuestas en orden aleatorio

**Para ficheros con  preguntas escribirme.**

![Ejemplo programa tests](fotos/ejemplo.png)

***
**Updates**:



***

## Instrucciones de uso
Descargar el repositorio

En una terminal, situarse en el directorio con los ficheros

Ejecutar: python3 test_app.py

## Formas de añadir tus propias preguntas

Para los json creados:

{

    "idx": {
        "q": "Pregunta",
        "op": 
        [
            "Pregunta 1",
            "Pregunta 2",
            "...",
            "Pregunta n"
        ],
        "ok": opcion correcta (1, 2, ..., n)
    }
}

* Idx es el numero de pregunta, debe ser el siguiente al ultimo ya puesto, no admite repetidos.
* En las preguntas acepta un maximo de 8 respuestas.
* La opcion correcta debe ser solo un numero. 
----x----

Se puede usar de ejemplo los json de la carpeta preguntas.



