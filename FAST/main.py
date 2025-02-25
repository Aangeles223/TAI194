from fastapi import FastAPI, HTTPException
from typing import Optional, List
from models import modelUsuario

app = FastAPI(
    title="Mi primer API", 
    Description="Aaron Angeles Chavez",
    version="2.0.0"
)

lista=[
    {"id":1, "nombre":"Aaron","edad":22,"correo":"aaron@gmail.com"},
    {"id":2, "nombre":"Alfredo","edad":23,"correo":"alfredo00@hotmail.com"},
    {"id":3, "nombre":"Angel","edad":20,"correo":"aangel23@yahoo.com"},
    {"id":4, "nombre":"Perla","edad":21,"correo":"perla12@otloook.com"},
]

#ruta o EndPoint
@app.get("/", tags=['Inicio'])
def main():
    return{"HELLO": "Hello World"}

#EndPoint CONSULTA TODOS
@app.get("/todosLista", response_model=List[modelUsuario], tags=['Operaciones CRUD'])
def leer():
    return lista

#EndPoint POST
@app.post("/lista/", response_model= modelUsuario, tags=['Operaciones CRUD'])
def insert(usuario:modelUsuario):
    for usr in lista:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400,detail="El usuario ya existe")
    
    lista.append(usuario.dict())
    return usuario


#EndPoint PUT
@app.put("/lista2/{id}", response_model= modelUsuario, tags=['Operaciones CRUD'])
def actualizar(id:int,usuarioActualizado:modelUsuario):
    for index, usr in enumerate(lista):
        if usr["id"] == id:
            lista[index] = usuarioActualizado.model_dump()
            return lista[index]
    raise HTTPException(status_code=400,detail="El usuario no existe")       


#EndPoint DELETE
@app.delete("/lista2/{id}", tags=['Operaciones CRUD'])
def borrar(id:int):
    for index, usr in enumerate(lista):
        if usr["id"] == id:
            lista.pop(index)
            return{"Lista Registrado": lista}
    raise HTTPException(status_code=400,detail="El usuario no existe")  