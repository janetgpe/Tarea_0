# Tarea 0
# Crear una ruta en Render llamada tarea-0. Casos a evaluar: 1.
# Dicha ruta será accesible por un método GET.
# Como respuesta, dicha ruta debe regresar lo siguiente (copialo y pégalo):
# {"respuesta": "Primer tarea realizada"}

import requests

def tarea_0():
    respuesta = requests.get("http://127.0.0.1:8000/tarea-0")
    print(respuesta.text)
   

tarea_0()