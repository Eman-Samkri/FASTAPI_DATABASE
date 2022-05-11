from weather import schemas,models
from sqlalchemy.orm import Session

def create(db:Session, request:schemas.Country):
    new_country = models.Country(country_name = request.country_name, capital_city = request.capital_city)
    db.add(new_country)
    db.commit()
    db.refresh(new_country)
    return new_country

def show (db:Session):
    contries = db.query(models.Country).all()
    return contries