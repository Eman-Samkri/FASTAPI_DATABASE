from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

class Weather(BaseModel):
    city_name:str
    temperature:float
    pressure : float
    humidity : float
    description:str

class ResponseModel(BaseModel):
    msg : str
    content : List[Weather]