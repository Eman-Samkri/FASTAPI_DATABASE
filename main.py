from fastapi import FastAPI , Depends
from weather import  models
from weather.database import engine , SessionLocal
from weather.schemas import ResponseModel,Weather
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
@app.get("/")
def index():
    return {"msg":"This is the index , or the home page"}


#http Method Post / create
@app.post("/city/create")
def create_new_city(request:Weather , db: Session = Depends(get_db)):
    new_city = models.Weather(city_name = request.city_name, temperature = request.temperature, 
    pressure = request.pressure, humidity = request.humidity, description = request.description)
    db.add(new_city)
    db.commit()
    db.refresh(new_city)
    return new_city

#http Method Get /  view all the cities with the weather temperature
@app.get("/weather")
def all_cities_weather (db: Session = Depends(get_db)):
    cities_weather = db.query(models.Weather).all()
    return cities_weather


#http Method GET with path parameters
@app.get('/weather/{city_id}')
def city_weather(city_id,db: Session = Depends(get_db)):
    city = db.query(models.Weather).filter(models.Weather.id == city_id).first()
    return city


@app.delete("/city/delete/{city_id}")
def delete_user(city_id,db: Session = Depends(get_db)):
    db.query(models.Weather).filter(models.Weather.id == city_id).delete(synchronize_session=False)
    db.commit()
    return "city deleted"


'''

#http Method Put / update
@app.put("/city/update/{index}", response_model=ResponseModel)
def update_city(weather:CityWeather, index:int):
    cities_weather[index] = weather
    return ResponseModel(msg="Update city weather successfully", content=cities_weather)


'''
