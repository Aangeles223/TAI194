from fastapi import FastAPI,HTTPException
from typing import Optional
from models import modelVehiculo


app = FastAPI(
    title="Mi primer API", 
    Description="Aaron Angeles Chavez",
    version="2.0.0"
)

Vehiculos=[
    {"id":1, "Modelo":"Ford","Ano":2000,"Placa":"HJK-123"},
    {"id":2, "Modelo":"Mercedes","Ano":2003,"Placa":"ASK-133"},
    {"id":3, "Modelo":"Alfa Romero","Ano":2010,"Placa":"KCJ-453"},
    {"id":4, "Modelo":"Chevrolet","Ano":2001,"Placa":"PZB-098"}
]

#EndPoint CONSULTA TODOS
@app.get("/todosvehiculo", tags=['Operaciones CRUD'])
def leer():
    return{"Lista Registrado": Vehiculos}

# EndPoint POST para guardar un vehículo
@app.post("/vehiculos/", tags=['Operaciones CRUD'])
def insert(vehiculo: modelVehiculo):
    for veh in Vehiculos:
        if veh["id"] == vehiculo.id:
            raise HTTPException(status_code=400, detail="El vehiculo ya existe")
    
    Vehiculos.append(vehiculo.dict())
    return vehiculo


#EndPoint POST
@app.put("/vehiculo/{id}", tags=['Operaciones CRUD'])
def actualizar(id:int,usuarioActualizado:dict):
    for index, usr in enumerate(Vehiculos):
        if usr["id"] == id:
            Vehiculos[index].update(usuarioActualizado)
            return  Vehiculos[index]
    raise HTTPException(status_code=400,detail="El Vehiculo no existe") 