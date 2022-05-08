from fastapi import FastAPI
from weather import  models
from weather.database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)

#http Method GET
@app.get("/")
def index():
    return {"msg":"This is the index , or the home page"}

'''
#http Method Get /  view all the cities with the weather temperature
@app.get("/weather", response_model=ResponseModel)
def get_cities_weather():
    return ResponseModel(msg="All cities weather", content=cities_weather)


#http Method GET with path parameters
@app.get("/weather/{city_name}")
def index(city_name : str):
    return {"msg": f"the weather of {city_name} is {cities_weather}"}


#http Method Post / create
@app.post("/city/create", response_model=ResponseModel)
def create_new_city(weather : CityWeather ):
    cities_weather.append(weather)
    return ResponseModel(msg="Added new city with weather", content=cities_weather)


#http Method Put / update
@app.put("/city/update/{index}", response_model=ResponseModel)
def update_city(weather:CityWeather, index:int):
    cities_weather[index] = weather
    return ResponseModel(msg="Update city weather successfully", content=cities_weather)

@app.delete("/city/delete/{index}", response_model=ResponseModel)
def delete_user(index:int):
    del cities_weather[index]
    return ResponseModel(msg=f"deleted city with id: {index}", content=cities_weather)

'''
