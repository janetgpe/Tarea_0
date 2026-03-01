# Tarea 0
# Crear una ruta en Render llamada tarea-0. Casos a evaluar: 1.
# Dicha ruta será accesible por un método GET.
# Como respuesta, dicha ruta debe regresar lo siguiente (copialo y pégalo):
# {"respuesta": "Primer tarea realizada"} 
# https://github.com/janetgpe/Tarea_0.git cuando ya se sube a github

from fastapi import FastAPI

app=FastAPI()

@app.get("/tarea-0")
def tarea_0_wrapper():
    return {"respuesta": "Primer tarea realizada"}



