from typing import List
from fastapi import FastAPI
from pydantic import BaseModel


class Weather(BaseModel):
    city_name:str
    temperature:float
    pressure : float
    humidity : float
    description:str

    class Config():
        orm_mode = True


class ShowCountry(BaseModel):
    country_name:str
    cities : List[Weather] =[]

    class Config:
        orm_mode = True



class ShowWeather(BaseModel):
    city_name :str
    temperature:float
    creator : ShowCountry

    class Config:
        orm_mode = True

class Country(BaseModel):
    country_name:str
    capital_city:str
    
