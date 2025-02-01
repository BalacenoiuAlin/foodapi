from sqlalchemy.orm import Session
from models import Food
from schemas import FoodCreate

def get_foods(db: Session):
    return db.query(Food).all()

def create_food(db: Session, food: FoodCreate):
    db_food = Food(**food.dict())
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food

def delete_food(db: Session, food_id: int):
    food = db.query(Food).filter(Food.id == food_id).first()
    if food:
        db.delete(food)
        db.commit()
        return True
    return False
