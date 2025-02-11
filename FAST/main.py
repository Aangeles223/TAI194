from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title="Mi primer API", 
    Description="Aaron Angeles Chavez",
    version="2.0.0"
)

lista=[
    {"id":1, "nombre":"Aaron","edad":22},
    {"id":2, "nombre":"Alfredo","edad":23},
    {"id":3, "nombre":"Angel","edad":20},
    {"id":4, "nombre":"Perla","edad":21}
]

#ruta o EndPoint
@app.get("/", tags=['Inicio'])
def main():
    return{"HELLO": "Hello World"}

#EndPoint CONSULTA TODOS
@app.get("/todosLista", tags=['Operaciones CRUD'])
def leer():
    return{"Lista Registrado": lista}

#EndPoint POST
@app.post("/lista/", tags=['Operaciones CRUD'])
def insert(usuario:dict):
    for usr in lista:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400,detail="El usuario ya existe")
    
    lista.append(usuario)
    return usuario


#EndPoint POST
@app.put("/lista2/{id}", tags=['Operaciones CRUD'])
def actualizar(id:int,usuarioActualizado:dict):
    for index, usr in enumerate(lista):
        if usr["id"] == id:
            lista[index].update(usuarioActualizado)
            return lista[index]
    raise HTTPException(status_code=400,detail="El usuario no existe")       