from fastapi import FastAPI
from DB.conexion import engine, Base
from Routers.usuarios import routerUsuario
from Routers.auth import routerAuth

app = FastAPI(
    title="Mi primer API", 
    Description="Aaron Angeles Chavez",
    version="2.0.0"
)

Base.metadata.create_all(bind=engine)

#ruta o EndPoint
@app.get("/", tags=['Inicio'])
def main():
    return{"HELLO": "Hello World"}

app.include_router(routerUsuario)
app.include_router(routerAuth)


