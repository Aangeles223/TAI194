from fastapi.responses import JSONResponse
from modelsPydantic import modelAuth
from genToken import createToken


from fastapi import APIRouter

routerAuth = APIRouter()

#ruta o EndPoint
@routerAuth.post("/auth", tags=['Autentificacion'])
def login(credenciales:modelAuth):
    if credenciales.mail == 'asasas@gmail.com' and credenciales.passw == '123456789':
        token: str = createToken(credenciales.model_dump())
        print(token)
        return JSONResponse(content= token)
    else:
        return{"Error": "Credenciales incorrectas"}
