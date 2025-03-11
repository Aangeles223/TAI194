from pydantic import BaseModel, Field

class modelVehiculo(BaseModel):
    id: int = Field(..., gt=0, description="ID siempre debe ser positivo")
    Modelo: str = Field(..., min_length=4, max_length=25, description="solo letras y espacios min 4 max 25")
    Ano: int = Field(..., ge=1000, le=9999, description="Año debe ser un número de 4 dígitos")
    Placa: str = Field(..., min_length=1, max_length=10, description="Placa debe tener entre 1 y 10 caracteres")