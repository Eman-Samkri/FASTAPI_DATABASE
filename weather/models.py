
from sqlalchemy import Column, Integer, String, Float,ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Country(Base):
    __tablename__ = 'country'

    country_id = Column(Integer, primary_key=True, index=True)
    country_name = Column(String)
    capital_city = Column(String)
    city_id = Column(Integer,ForeignKey("weather.city_id"))
    creator = relationship("Weather", back_populates="cities")


class Weather(Base):
    __tablename__ = 'weather'

    city_id = Column(Integer, primary_key=True, index=True)
    city_name = Column(String)
    temperature = Column(Float)
    pressure = Column(Float)
    humidity = Column(Float)
    description=  Column(String)
    cities = relationship("Country", back_populates="creator")

