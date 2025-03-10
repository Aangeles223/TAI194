from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List
from models import modelUsuario, modelAuth
from genToken import createToken
from middlewares import BearerJWT


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

#ruta o EndPoint
@app.post("/auth", tags=['Autentificacion'])
def login(credenciales:modelAuth):
    if credenciales.mail == 'asasas@gmail.com' and credenciales.passw == '123456789':
        token: str = createToken(credenciales.model_dump())
        print(token)
        return JSONResponse(content= token)
    else:
        return{"Error": "Credenciales incorrectas"}

# Enpoint CONSULTA TODOS
@app.get("/todosUsuarios/", response_model=List[modelUsuario], tags=['Operaciones CRUD'])
def leer(token: dict = Depends(BearerJWT())):
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