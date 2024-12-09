from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Flavor, Ingredient, Allergen, Suggestion, SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add_flavor/")
def add_flavor(name: str, ingredients: str, db: Session = Depends(get_db)):
    flavor = Flavor(name=name, ingredients=ingredients)
    db.add(flavor)
    db.commit()
    return {"message": "Flavor added successfully!"}

@router.get("/view_flavors/")
def view_flavors(db: Session = Depends(get_db)):
    return db.query(Flavor).all()

@router.post("/add_allergen/")
def add_allergen(name: str, db: Session = Depends(get_db)):
    allergen = Allergen(name=name)
    db.add(allergen)
    db.commit()
    return {"message": "Allergen added successfully!"}
