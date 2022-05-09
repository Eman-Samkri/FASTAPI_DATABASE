from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

class Weather(BaseModel):
    city_name:str
    temperature:float
    pressure : float
    humidity : float
    description:str

class ShowCity(BaseModel):
    city_name :str
    temperature:float

    class Config:
        orm_mode = True