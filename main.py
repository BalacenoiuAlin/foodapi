from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import Food
from schemas import FoodCreate, FoodResponse
from crud import get_foods, create_food, delete_food
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Merge!"}

@app.post("/foods/", response_model=FoodResponse)
def add_food(food: FoodCreate, db: Session = Depends(get_db)):
    return create_food(db, food)

@app.get("/foods/", response_model=List[FoodResponse])
def list_foods(db: Session = Depends(get_db)):
    return get_foods(db)

@app.delete("/foods/{food_id}")
def remove_food(food_id: int, db: Session = Depends(get_db)):
    if not delete_food(db, food_id):
        raise HTTPException(status_code=404, detail="Food not found")
    return {"message": "Food deleted"}
