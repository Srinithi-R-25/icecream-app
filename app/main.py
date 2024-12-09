from fastapi import FastAPI, HTTPException, Query, Body
from pydantic import BaseModel
from typing import List

# Initialize the FastAPI app
app = FastAPI()

# In-memory data
flavors = [
    {"id": 1, "name": "Vanilla", "ingredients": ["Milk", "Sugar"], "availability": True},
    {"id": 2, "name": "Chocolate", "ingredients": ["Cocoa", "Milk"], "availability": True},
]

ingredients = [
    {"id": 1, "name": "Milk", "stock": 100},
    {"id": 2, "name": "Sugar", "stock": 50},
    {"id": 3, "name": "Cocoa", "stock": 30},
]

allergens = ["Peanuts", "Gluten"]

cart = []

# Pydantic models
class FlavorRequest(BaseModel):
    name: str
    ingredients: List[str]

class AddToCartRequest(BaseModel):
    flavor_id: int

class AllergenRequest(BaseModel):
    allergen: str

# Routes

@app.get("/")
def root():
    return {
        "welcome_message": "Welcome to the Ice Cream Parlor API!",
        "instructions": "Use /docs to explore the API documentation.",
        "available_endpoints": {
            "View Flavors": "/flavors/",
            "Add Flavor": "/add_flavor/",
            "Add Allergen": "/add_allergen/",
            "View Cart": "/cart/",
            "Add to Cart": "/cart/add/",
            "Search Flavors": "/search_flavors/",
        },
    }

@app.get("/flavors/")
def get_flavors():
    return {"flavors": flavors}

@app.post("/add_flavor/")
def add_flavor(flavor: FlavorRequest):
    # Check for duplicate flavors
    if any(f["name"].lower() == flavor.name.lower() for f in flavors):
        raise HTTPException(status_code=400, detail="Flavor already exists")

    new_flavor = {
        "id": len(flavors) + 1,
        "name": flavor.name,
        "ingredients": flavor.ingredients,
        "availability": True,
    }
    flavors.append(new_flavor)
    return {"message": "Flavor added successfully!", "flavor": new_flavor}

@app.get("/cart/")
def view_cart():
    return {"cart": cart}

@app.post("/cart/add/")
def add_to_cart(request: AddToCartRequest):
    flavor = next((f for f in flavors if f["id"] == request.flavor_id), None)
    if not flavor:
        raise HTTPException(status_code=404, detail="Flavor not found")
    cart.append(flavor)
    return {"message": "Flavor added to cart", "cart": cart}

@app.post("/add_allergen/")
def add_allergen(request: AllergenRequest):
    if request.allergen.lower() in (a.lower() for a in allergens):
        raise HTTPException(status_code=400, detail="Allergen already exists")
    allergens.append(request.allergen)
    return {"message": "Allergen added successfully", "allergens": allergens}

@app.get("/search_flavors/")
def search_flavors(keyword: str):
    # Convert the keyword to lowercase and search for matching flavor names
    results = [f for f in flavors if keyword.lower() in f["name"].lower()]
    
    # If no results found, return a message
    if not results:
        return {"message": "No flavors found", "results": []}
    
    return {"results": results}

