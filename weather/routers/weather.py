from typing import List
from fastapi import APIRouter, Depends, status, Response
from weather import schemas,models,database
from sqlalchemy.orm import Session

router = APIRouter(
prefix="/city",
tags=["weather"]
)

#http Method Get /  view all the cities with the weather temperature
@router.get("/weather", response_model= List[schemas.ShowWeather])
def all_cities_weather (db: Session = Depends(database.get_db)):
    cities_weather = db.query(models.Weather).all()
    return cities_weather


#http Method Post / create
@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_new_city(request:schemas.Weather , db: Session = Depends(database.get_db)):
    new_city = models.Weather(city_name = request.city_name, temperature = request.temperature, 
    pressure = request.pressure, humidity = request.humidity, description = request.description, country_id = 1)
    db.add(new_city)
    db.commit()
    db.refresh(new_city)
    return new_city



#http Method GET with path parameters
@router.get('/weather/{city_id}', status_code=status.HTTP_200_OK)
def city_weather(city_id,response: Response, db: Session = Depends(database.get_db)):
    city = db.query(models.Weather).filter(models.Weather.city_id == city_id).first()
    if not city:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detils": f"the city with id {city_id} not found"}
    return city


@router.delete("/delete/{city_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(city_id, response: Response, db: Session = Depends(database.get_db)):
    city = db.query(models.Weather).filter(models.Weather.city_id == city_id)
    if not city.first():
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detils": f"the city with id {city_id} not found"}
    city.delete(synchronize_session=False)
    db.commit()


#http Method Put / update
@router.put("/update/{city_id}", status_code= status.HTTP_202_ACCEPTED)
def update_city(city_id, response: Response, request:schemas.Weather, db: Session = Depends(database.get_db)):
   city = db.query(models.Weather).filter(models.Weather.city_id == city_id)
   if not city.first():
       response.status_code = status.HTTP_404_NOT_FOUND
       return 'not found the city to updated'
   city.update({'city_name':request.city_name,
   'temperature':request.temperature, 'pressure':request.pressure, 'humidity':request.humidity, 'description':request.description})
   db.commit()
   return 'updated'
