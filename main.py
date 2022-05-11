from typing import List
from fastapi import FastAPI , Depends, status , Response
from weather import  models , schemas
from weather.database import engine , get_db
from sqlalchemy.orm import Session
from weather.routers import weather, country

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(weather.router)
app.include_router(country.router)


#http Method GET
@app.get("/", tags=["Home"])
def index():
    return {"msg":"This is the index , or the home page"}




