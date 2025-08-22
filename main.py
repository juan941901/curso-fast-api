import zoneinfo
from datetime import datetime

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"mesasge" : "Hola, Juan"}

@app.get("/hora")
async def time():
    return {"time" : datetime.now()}

zona_horaria_paises = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}

@app.get("/hora_por_zona/{zona_horaria}")
async def time(zona_horaria: str):

    iso = zona_horaria.upper()
    zona_horaria_str = zona_horaria_paises.get(iso)
    tz = zoneinfo.ZoneInfo(zona_horaria_str)
    return {"time" : datetime.now(tz)}

# ------------ Peticion POST ---------------------
from pydantic import BaseModel

class Customer(BaseModel):
    nombre : str
    descripcion: str | None
    edad : int
    correo : str

@app.post("/creacion_cliente")
async def create_customer(costumer_data : Customer):
    return costumer_data