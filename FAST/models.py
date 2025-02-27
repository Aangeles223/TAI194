from pydantic import BaseModel, Field, EmailStr

class modelUsuario(BaseModel):
    id:int = Field(..., gt=0, description="ID siempre debe ser positivo")
    nombre:str = Field(..., min_lenth=1, max_length=85, description="solo letras y espacios min 1 max 85") 
    edad:int =  Field(...,gt=0, le=100, description="siempre debe ser la edad positivo y mayor a 0")
    correo:str = Field(...,pattern=r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,6}$', description="correo electronico de de contar con un @" )

class modelAuth(BaseModel):
    mail: EmailStr = Field(..., description="correo electronico de de contar con un @" )
    passw:str = Field(..., min_lenth=8, strip_whitespace=True , description="solo letras sin espacios min 8") 
    