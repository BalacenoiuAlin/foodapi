from pydantic import BaseModel

class FoodCreate(BaseModel):
    name: str
    calories: float
    proteins: float
    carbs: float
    fats: float

class FoodResponse(FoodCreate):
    id: int

    class Config:
        from_attributes = True
