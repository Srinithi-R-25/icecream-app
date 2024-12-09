1) Created a folder named icecream-app which consists of files
      ->app(Backend directory)
          main.py(FastAPI backend logic)
          models.py(SQLAlchemy database models)
          routes.py(API route definitions)
      ->frontend
          app.py(Streamlit app file)
      ->Dockerfile
      ->requirements.txt(dependencies for the project)    


app(Backend directory)
 main.py - It helps you to manage an ice cream parlor's menu, cart, and allergens. You can view, add, and search for ice cream flavors, add items to your cart, and add allergens if they're not already in the system. 

models.py - This code tells us the database structure for the ice cream parlor app, including tables for flavors, ingredients, allergens etc, It uses SQLAlchemy to connect to a SQLite database and sets up the necessary relationships between the tables. The database is initialized and ready to store data for the app.
FlavorRequest: Used to define the structure of a flavor (name and ingredients) for requests to add a flavor.
AddToCartRequest: Defines the request structure for adding a flavor to the cart.
AllergenRequest: Defines the request structure for adding allergens.

routes.py - This code sets up the routes for adding new ice cream flavors and allergens to the database. It uses SQLAlchemy to interact with the database and handles the addition of flavors and allergens. The routes allow for adding flavors and viewing all available flavors from the database.
/: The root endpoint, which gives instructions and available endpoints.
/flavors/: Returns the list of all available ice cream flavors.
/add_flavor/: Adds a new flavor to the system after checking for duplicates.
/cart/: Returns the current contents of the cart.
/cart/add/: Adds a selected flavor to the cart.
/add_allergen/: Adds a new allergen to the system if it doesn't already exist.
/search_flavors/: Searches for flavors based on the provided keyword.

 frontend

 app.py - creates a Streamlit app that interacts with the FastAPI backend to manage ice cream flavors, allergens, and a shopping cart. Users can view, add, search for flavors, manage their cart, and add allergens.
 Design-A sidebar allows users to navigate between different sections of the app, including View Flavors, Add Flavor, Search Flavors, Manage Cart, and Add Allergen.

 # COMMANDS FOR RUNNING THE APPLICATION

 Frontend application:
 1) change the directory to icecream-app
 2) cd frontend
 3) streamlit run app.py
 
 backend server:
 1) pip install -r requirements.txt
 2) uvicorn app.main:app --reload
  
 Docker commands
 1) docker build -t icecream-app .
 2) docker run -d --name icecream-app-container -p 8000:8000 -p 8502:8502 icecream-app
 When the Docker container is run, the backend and frontend are both launched:

Backend runs at http://127.0.0.1:8000.
Frontend runs at http://localhost:8502.



