from typing import List
from fastapi import FastAPI , Depends, status , Response
from weather import  models , schemas
from weather.database import engine , SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#http Method GET
@app.get("/", tags=["Home"])
def index():
    return {"msg":"This is the index , or the home page"}


#http Method Post / create
@app.post("/city/create", status_code=status.HTTP_201_CREATED, tags=["weather"])
def create_new_city(request:schemas.Weather , db: Session = Depends(get_db)):
    new_city = models.Weather(city_name = request.city_name, temperature = request.temperature, 
    pressure = request.pressure, humidity = request.humidity, description = request.description, country_id = 1)
    db.add(new_city)
    db.commit()
    db.refresh(new_city)
    return new_city

#http Method Get /  view all the cities with the weather temperature
@app.get("/weather", response_model= List[schemas.ShowWeather],tags=["weather"])
def all_cities_weather (db: Session = Depends(get_db)):
    cities_weather = db.query(models.Weather).all()
    return cities_weather


#http Method GET with path parameters
@app.get('/weather/{city_id}', status_code=status.HTTP_200_OK, tags=["weather"])
def city_weather(city_id,response: Response, db: Session = Depends(get_db)):
    city = db.query(models.Weather).filter(models.Weather.city_id == city_id).first()
    if not city:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detils": f"the city with id {city_id} not found"}
    return city


@app.delete("/city/delete/{city_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["weather"])
def delete_user(city_id, response: Response, db: Session = Depends(get_db)):
    city = db.query(models.Weather).filter(models.Weather.id == city_id)
    if not city.first():
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detils": f"the city with id {city_id} not found"}
    city.delete(synchronize_session=False)
    db.commit()


#http Method Put / update
@app.put("/city/update/{city_id}", status_code= status.HTTP_202_ACCEPTED, tags=["weather"])
def update_city(city_id, response: Response, request:schemas.Weather, db: Session = Depends(get_db)):
   city = db.query(models.Weather).filter(models.Weather.id == city_id)
   if not city.first():
       response.status_code = status.HTTP_404_NOT_FOUND
       return 'not found the city to updated'
   city.update({'city_name':request.city_name,
   'temperature':request.temperature, 'pressure':request.pressure, 'humidity':request.humidity, 'description':request.description})
   db.commit()
   return 'updated'

   ###########################################################################################

   #http Method Post / create
@app.post("/country/create", status_code=status.HTTP_201_CREATED, tags=["Country"])
def create_new_country(request:schemas.Country , db: Session = Depends(get_db)):
    new_country = models.Country(country_name = request.country_name, capital_city = request.capital_city)
    db.add(new_country)
    db.commit()
    db.refresh(new_country)
    return new_country

#http Method Get /  view all the cities with the weather temperature
@app.get("/country", response_model= List[schemas.ShowCountry],tags=["Country"])
def all_contries (db: Session = Depends(get_db)):
    contries = db.query(models.Country).all()
    return contries

