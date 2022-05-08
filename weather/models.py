
from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True, index=True)
    city_name = Column(String)
    temperature = Column(Float)
    pressure = Column(Float)
    humidity = Column(Float)
    description=  Column(String)

