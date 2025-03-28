from fastapi import  HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from modelsPydantic import modelUsuario
from DB.conexion import Session
from models.modelsDB import User


from fastapi import APIRouter

routerUsuario = APIRouter()


# Enpoint CONSULTA TODOS
@routerUsuario.get("/todosUsuarios/", tags=['Operaciones CRUD'])
def leer():
    db=Session()

    try:
        consulta= db.query(User).all()
        return JSONResponse(content= jsonable_encoder(consulta))
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"message": "No fue posible la consulta",
                                     "error": str(e) })
    
    finally:
        db.close()



# Enpoint buscar por id
@routerUsuario.get("/idUsuarios/{id}", tags=['Operaciones CRUD'])
def Buscar(id:int):
    db=Session()

    try:
        consulta1= db.query(User).filter(User.id == id).first()
        if not consulta1:
            return JSONResponse(status_code=404, content={"mensaje":"Usuario no encontrado"})
        
        return JSONResponse(content= jsonable_encoder(consulta1))
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"message": "No fue posible encontrar al usuario",
                                     "error": str(e) })
    
    finally:
        db.close()


#EndPoint POST
@routerUsuario.post("/lista/", response_model= modelUsuario, tags=['Operaciones CRUD'])
def insert(usuario:modelUsuario):
    db=Session()
    try:
        db.add(User(**usuario.model_dump()))
        db.commit()
        return JSONResponse(status_code=201,
                            content={"message": "usuario Guardado",
                                    "usuario": usuario.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"message": "No fue posible guardar",
                                     "error": str(e) })
    finally:
        db.close()


#EndPoint PUT Actualizar usuario
@routerUsuario.put("/lista2/{id}", response_model= modelUsuario, tags=['Operaciones CRUD'])
def actualizar(id:int,usuarioActualizado:modelUsuario):
    db=Session()
    try:
        usuario_db = db.query(User).filter(User.id == id).first()
        if not usuario_db:
            raise HTTPException(status_code=404, detail="El usuario no existe")
        
        usuario_db.name = usuarioActualizado.name
        usuario_db.age = usuarioActualizado.age
        usuario_db.email = usuarioActualizado.email

        db.commit()
        db.refresh(usuario_db)
        return JSONResponse(status_code=201,
                            content={"message": "usuario Actualizado Correctamente",
                                    "usuario": jsonable_encoder(usuario_db)})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"message": "No fue posible actualizar",
                                     "error": str(e) })
    finally:
        db.close()
    for index, usr in enumerate(lista):
        if usr["id"] == id:
            lista[index] = usuarioActualizado.model_dump()
            return lista[index]
    raise HTTPException(status_code=400,detail="El usuario no existe")       


#EndPoint DELETE Usuario
@routerUsuario.delete("/lista2/{id}", tags=['Operaciones CRUD'])
def borrar(id:int):
    db=Session()
    try:
        usuario_db = db.query(User).filter(User.id == id).first()
        if not usuario_db:
            raise HTTPException(status_code=404, detail="El usuario no existe")
        
        db.delete(usuario_db)
        db.commit()
        
        return JSONResponse(status_code=201,
                            content={"message": "usuario eliminado",
                                    "usuario": jsonable_encoder(usuario_db)})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"message": "No fue posible elimiar el usuario",
                                     "error": str(e) })
    finally:
        db.close()
    #for index, usr in enumerate(lista):
      #  if usr["id"] == id:
       #     lista.pop(index)
        #    return{"Lista Registrado": lista}
    #raise HTTPException(status_code=400,detail="El usuario no existe")  