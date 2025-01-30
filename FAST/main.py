from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def main():
    return{"HELLO": "Hello World"}


#EndPoint promedio
@app.get("/promedio")
def promedio():
    return 10.5


#EndPoint con parametro obligatorio
@app.get("/usuario/{id}")
def consultausuario(id:int):
    #caso ficticia de busqueda en BD
    return {"Se encontro el usuario":id}