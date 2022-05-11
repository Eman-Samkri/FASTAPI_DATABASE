from typing import List
from fastapi import APIRouter, Depends, status, Response
from weather import schemas,models,database
from sqlalchemy.orm import Session
from weather.repository import weather

router = APIRouter(
prefix="/city",
tags=["weather"]
)

#http Method Get /  view all the cities with the weather temperature
@router.get("/weather", response_model= List[schemas.ShowWeather])
def all_cities_weather (db: Session = Depends(database.get_db)):
   return weather.show(db)


#http Method Post / create
@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_new_city(request:schemas.Weather , db: Session = Depends(database.get_db)):
    return weather.create(db, request)



#http Method GET with path parameters
@router.get('/weather/{city_id}', status_code=status.HTTP_200_OK)
def city_weather(city_id,response: Response, db: Session = Depends(database.get_db)):
    return weather.get_city(city_id, db, response)


@router.delete("/delete/{city_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(city_id, response: Response, db: Session = Depends(database.get_db)):
    return weather.delete(city_id, db, response)


#http Method Put / update
@router.put("/update/{city_id}", status_code= status.HTTP_202_ACCEPTED)
def update_city(city_id, response: Response, request:schemas.Weather, db: Session = Depends(database.get_db)):
   return weather.update(city_id, db, response, request)
