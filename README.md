# Test_Repaso

Una aplicación de consola interactiva en Python para crear y realizar tests de repaso con preguntas aleatorias y respuestas en orden aleatorio.

![Ejemplo del programa](fotos/ejemplo.png)

## Tabla de Contenidos

- [Características](#características)
- [Requisitos del Sistema](#requisitos-del-sistema)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Formato de Preguntas](#formato-de-preguntas)
- [Añadir Tus Propias Preguntas](#añadir-tus-propias-preguntas)
- [Funcionalidades](#funcionalidades)
- [Contribuir](#contribuir)
- [Registro de Cambios](#registro-de-cambios)
- [Licencia](#licencia)
- [Autor](#autor)

## Características

- **Preguntas aleatorias**: Las preguntas se presentan en orden aleatorio
- **Respuestas mezcladas**: Las opciones de respuesta se muestran en orden aleatorio
- **Sistema de puntuación**: Seguimiento de aciertos, fallos y preguntas no contestadas
- **Repetición inteligente**: Opción de repetir solo las preguntas falladas y no contestadas
- **Organización por asignaturas**: Sistema de categorías y subcategorías
- **Multiplataforma**: Compatible con Windows, Linux y macOS

## Requisitos del Sistema

- **Python**: 3.6 o superior
- **Sistema Operativo**: Windows, Linux, macOS
- **Dependencias**: Ver `requirements.txt`

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/HugoVarelaSanchez/Test_Repaso.git
   cd Test_Repaso
   ```

2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación**:
   ```bash
   python3 test_app.py
   ```

## Uso

### Inicio Rápido

1. Ejecuta `python3 test_app.py`
2. Selecciona la asignatura deseada
3. Elige la categoría y el test específico
4. Indica el número de preguntas que quieres contestar
5. Responde usando las letras `a`, `b`, `c`, `d`, etc.
6. Usa `s` para saltar una pregunta
7. Al finalizar, revisa tu puntuación y decide si repetir las falladas

### Controles

- **Letras (a-h)**: Seleccionar respuesta
- **s**: Saltar pregunta
- **r**: Retroceder en los menús
- **Enter**: Continuar
- **Ctrl+C**: Salir del programa

## Estructura del Proyecto

```
Test_Repaso/
├── asignaturas/             # Carpeta principal de contenido
│   ├── ICAP/
│   │   └── Teoria/
│   │       └── icap.json
│   └── MEDAD/
│       └── Ejercicios/
│           └── medad.json
├── fotos/                   # Imágenes del proyecto
│   └── ejemplo.png
├── funciones/               # Módulos de Python
│   ├── aux_funcions.py      
│   ├── aux_preguntas.py     
│   ├── conversion_letras.py 
│   ├── os_functions.py      
│   └── Usuario.py           
├── test_app.py              # Archivo principal
├── requirements.txt         # Dependencias
├── LICENSE                  # Licencia GPL v3
└── README.md                # Este archivo
```

## Formato de Preguntas

Los archivos de preguntas utilizan formato JSON con la siguiente estructura:

```json
{

    "1": {
        "q": "¿Título la pregunta?",
        "op": [
            "Primera opción",
            "Segunda opción", 
            "Tercera opción",
            "Cuarta opción"
        ],
        "ok": 2
    },

    "2": {
        "q": "Otra pregunta...",
        "op": [
            "Opción A",
            "Opción B"
        ],
        "ok": 1
    }
}
```

### Especificaciones del Formato

- **`idx`**: Número de pregunta (debe ser consecutivo y único)
- **`q`**: Texto de la pregunta
- **`op`**: Array de opciones de respuesta (máximo 8 opciones)
- **`ok`**: Número de la opción correcta (1-8)


## Añadir Tus Propias Preguntas

### Método 1: Crear Nueva Asignatura

1. Crea una carpeta en `asignaturas/` con el nombre de tu asignatura
2. Dentro, crea subcarpetas para organizar por temas
3. Añade archivos `.json` con tus preguntas siguiendo el formato especificado

### Método 2: Añadir a Asignatura Existente

1. Navega a `asignaturas/[ASIGNATURA]/[CATEGORIA]/`
2. Crea un nuevo archivo `.json` o edita uno existente
3. Sigue el formato JSON especificado arriba

### Importante para Crear Preguntas

- Máximo 8 opciones de respuesta por pregunta
- La opción correcta debe ser solo un número (1-8)
- Usar nombres descriptivos para archivos y carpetas

> [!NOTE]
> Puedes usar los archivos `icap.json` y `medad.json` como ejemplos de referencia.

## Funcionalidades

### Sistema de Puntuación

- **Aciertos**: +1 / Total | por respuesta correcta
- **Fallos**: -0.5 / Total | en el cálculo final
- **No contestadas**: No penalizan pero no suman
- **Nota final**: `(Aciertos - Fallos/2) / Total * 10`

### Características Especiales

- **Test perfecto**: Animación especial al conseguir 10/10
- **Modo repetición**: Repite solo preguntas falladas/no contestadas
- **Interfaz visual**: Colores diferenciados para cada tipo de resultado
- **Estadísticas en tiempo real**: Ve tu progreso durante el test

> [!CAUTION]
> Si la nota calculada es negativa, se mostrará como 0 en el resultado final.

## Contribuir

¡Las contribuciones son bienvenidas! Si tienes preguntas para añadir o mejoras que sugerir:

**Para mejoras de código**: 
   - Fork el proyecto
   - Crea una rama para tu feature
   - Haz commit de tus cambios
   - Push a la rama
   - Abre un Pull Request

> [!NOTE]
> Para ficheros con preguntas, escríbeme directamente.

## Registro de Cambios

### Versión actual
- Base

## Licencia

Este proyecto está licenciado bajo la **Licencia Pública General GNU versión 3** (GPL v3).

Test_Repaso es software libre: puedes redistribuirlo y/o modificarlo bajo los términos de la Licencia Pública General GNU versión 3 publicada por la Free Software Foundation.

Test_Repaso se distribuye con la esperanza de que sea útil, pero SIN NINGUNA GARANTÍA; sin siquiera la garantía implícita de COMERCIABILIDAD o IDONEIDAD PARA UN PROPÓSITO PARTICULAR. Consulta la Licencia Pública General GNU para más detalles.

Consulta el archivo [LICENSE](LICENSE) para más detalles o visita [https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html).

## Autor

**Hugo Varela Sanchez** (HugoVarelaSanchez)
- GitHub: [https://github.com/HugoVarelaSanchez](https://github.com/HugoVarelaSanchez)
- Proyecto: [https://github.com/HugoVarelaSanchez/Test_Repaso](https://github.com/HugoVarelaSanchez/Test_Repaso)

---

¡Gracias por usar Test_Repaso y mucho ánimo con tus estudios! 📚
