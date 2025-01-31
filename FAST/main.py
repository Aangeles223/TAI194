from fastapi import FastAPI
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


@app.get("/", tags=['Inicio'])
def main():
    return{"HELLO": "Hello World"}


#EndPoint promedio
@app.get("/promedio", tags=['Mi calificacion'])
def promedio():
    return 10.5


#EndPoint con parametro obligatorio
@app.get("/usuario/{id}", tags=['Endpoint parametro obligatorio'])
def consultausuario(id:int):
    #caso ficticia de busqueda en BD
    return {"Se encontro el usuario":id}

#EndPoint con parametro opcional
@app.get("/usuario2/", tags=['Endpoint parametro opcional'])
def consultausuario2(id: Optional[int]=None):
    if id is not None:
        for usuario in lista:
            if usuario["id"] == id:
                return {"Mensaje":"usuario encontrado","El usuario es:":usuario}
        return {"mensaje":f"No se encontro el id: {id}"}
    return {"mensaje:":"No se proporciono un ID"}


    #endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in lista:
        if (
            (id is None or usuario["id"] == id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}