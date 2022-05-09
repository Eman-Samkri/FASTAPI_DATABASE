from typing import List
from fastapi import FastAPI
from pydantic import BaseModel


class Country(BaseModel):
    country_name:str
    capital_city:str


class Weather(BaseModel):
    city_name:str
    temperature:float
    pressure : float
    humidity : float
    description:str
    class Config:
        orm_mode = True

class ShowCity(BaseModel):
    city_name :str
    temperature:float

    class Config:
        orm_mode = True

class ShowCountry(BaseModel):
    country_name:str

    class Config:
        orm_mode = True