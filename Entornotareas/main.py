from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title="Tareas APIs", 
    Description="Aaron Angeles Chavez",
    version="2.0.1"
)

Tareas=[
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
@app.get("/", tags=['Inicio'])
def main():
    return{"HELLO": "Hello World"}

#EndPoint CONSULTA TODOS
@app.get("/todasTareas", tags=['Tareas'])
def leer():
    return{"Tareas Registradas": Tareas}

#Obtener tarea por id
@app.get("/tareas/", tags=['Tareas'])
def consultartarea(id: Optional[int]=None):
    if id is not None:
        for tarea in Tareas:
            if tarea["id"] == id:
                return {"Mensaje":"La tarea fue encontrado","La tarea es:":tarea}
        return {"mensaje":f"No se encontro el id de la tarea: {id}"}
    return {"mensaje:":"No se proporciono un ID"}

#EndPoint Crear una nueva tarea
@app.post("/Tareas/", tags=['Tareas'])
def insert(tarea:dict):
    for usr in Tareas:
        if usr["id"] == tarea.get("id"):
            raise HTTPException(status_code=400,detail="La tareas ya existe")
    
    Tareas.append(tarea)
    return tarea

#EndPoint Actualizar la tarea
@app.put("/Tareas/{id}", tags=['Tareas'])
def actualizar(id:int,tareaActualizada:dict):
    for index, usr in enumerate(Tareas):
        if usr["id"] == id:
            Tareas[index].update(tareaActualizada)
            return Tareas[index]
    raise HTTPException(status_code=400,detail="La tarea no existe")  

#EndPoint Eliminar tareas
@app.delete("/Tareas/{id}", tags=['Tareas'])
def borrar(id:int):
    for index, usr in enumerate(Tareas):
        if usr["id"] == id:
            Tareas.pop(index)
            return{"Tarea Registrada": Tareas}
    raise HTTPException(status_code=400,detail="La tarea no existe")  