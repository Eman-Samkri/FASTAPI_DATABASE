from typing import List
from fastapi import APIRouter, Depends, status
from weather import schemas,models,database
from sqlalchemy.orm import Session

router = APIRouter(
prefix="/country",
tags=["Country"]
)



   #http Method Post / create
@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_new_country(request:schemas.Country , db: Session = Depends(database.get_db)):
    new_country = models.Country(country_name = request.country_name, capital_city = request.capital_city)
    db.add(new_country)
    db.commit()
    db.refresh(new_country)
    return new_country

#http Method Get /  view all the cities with the weather temperature
@router.get("/show", response_model= List[schemas.ShowCountry])
def all_contries (db: Session = Depends(database.get_db)):
    contries = db.query(models.Country).all()
    return contries