from sqlalchemy import Column, Integer, String, Float
from database import Base

class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    calories = Column(Float, nullable=False)
    proteins = Column(Float, nullable=False)
    carbs = Column(Float, nullable=False)
    fats = Column(Float, nullable=False)
