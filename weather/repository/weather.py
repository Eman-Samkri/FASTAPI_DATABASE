from fastapi import Response,status
from weather import schemas,models
from sqlalchemy.orm import Session


def show(db:Session):
    cities_weather = db.query(models.Weather).all()
    return cities_weather

def create(db:Session, request:schemas.Weather):
    new_city = models.Weather(city_name = request.city_name, temperature = request.temperature, 
    pressure = request.pressure, humidity = request.humidity, description = request.description, country_id = 1)
    db.add(new_city)
    db.commit()
    db.refresh(new_city)
    return new_city

def get_city(city_id:int, db:Session, response:Response):
    city = db.query(models.Weather).filter(models.Weather.city_id == city_id).first()
    if not city:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detils": f"the city with id {city_id} not found"}
    return city


def delete(city_id:int, db:Session, response:Response):
    city = db.query(models.Weather).filter(models.Weather.city_id == city_id)
    if not city.first():
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detils": f"the city with id {city_id} not found"}
    city.delete(synchronize_session=False)
    db.commit()

def update(city_id:int, db:Session, response:Response, request:schemas.Weather):
    city = db.query(models.Weather).filter(models.Weather.city_id == city_id)
    if not city.first():
       response.status_code = status.HTTP_404_NOT_FOUND
       return 'not found the city to updated'
    city.update({'city_name':request.city_name,
   'temperature':request.temperature, 'pressure':request.pressure, 'humidity':request.humidity, 'description':request.description})
    db.commit()
    return 'updated'