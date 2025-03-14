from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title="Tareas APIs", 
    Description="Aaron Angeles Chavez",
    version="2.0.1"
)

Tarea=[
    {"id":1, 
     "titulo":"Estudiar para el examen",
     "descripcion":"Repasar los apuntes de TAI",
     "vencimiento":"14-02-24",
     "Estado":"completada"},

    {"id":2, 
     "titulo":"Estudiar para la exposicion",
     "descripcion":"Repasar los apuntes de de SW",
     "vencimiento":"17-02-24",
     "Estado":"no completada"},

    {"id":3, 
     "titulo":"Realizar actividad de TEC.Y.AP.EN.INT",
     "descripcion":"Realizar un programa con API",
     "vencimiento":"17-02-24",
     "Estado":"no completada"},

    {"id":4, 
     "titulo":"Hacer el quehacer",
     "descripcion":"hacer limpieza en casa",
     "vencimiento":"14-02-24",
     "Estado":"completada"}
]

#ruta o EndPoint
@app.get("/Entornotareas", tags=['Inicio'])
def main():
    return{"HELLO": "Hello World"}

#EndPoint CONSULTA TODOS
@app.get("/Tarea/", tags=['Tareas'])
def leer():
    return{"Tareas Registradas": Tarea}

#Obtener tarea por id
@app.get("/Tarea/{id}", tags=['Tareas'])
def consultartarea(id: Optional[int]=None):
    if id is not None:
        for tarea in Tarea:
            if tarea["id"] == id:
                return {"Mensaje":"La tarea fue encontrado","La tarea es:":tarea}
        return {"mensaje":f"No se encontro el id de la tarea: {id}"}
    return {"mensaje:":"No se proporciono un ID"}

#EndPoint Crear una nueva tarea
@app.post("/Tarea/", tags=['Tareas'])
def insert(tarea:dict):
    for usr in Tarea:
        if usr["id"] == tarea.get("id"):
            raise HTTPException(status_code=400,detail="La tareas ya existe")
    
    Tarea.append(tarea)
    return tarea

#EndPoint Actualizar la tarea
@app.put("/Tarea/{id}", tags=['Tareas'])
def actualizar(id:int,tareaActualizada:dict):
    for index, usr in enumerate(Tarea):
        if usr["id"] == id:
            Tarea[index].update(tareaActualizada)
            return Tarea[index]
    raise HTTPException(status_code=400,detail="La tarea no existe")  

#EndPoint Eliminar tareas
@app.delete("/Tarea/{id}", tags=['Tareas'])
def borrar(id:int):
    for index, usr in enumerate(Tarea):
        if usr["id"] == id:
            Tarea.pop(index)
            return{"Tarea Registrada": Tarea}
    raise HTTPException(status_code=400,detail="La tarea no existe")  