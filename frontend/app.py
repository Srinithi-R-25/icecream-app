import streamlit as st
import requests

# Backend base URL
BASE_URL = "http://127.0.0.1:8000"

# App Title
st.title("🍦 Ice Cream Parlor App")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio(
    "Go to:",
    ["View Flavors", "Add Flavor", "Search Flavors", "Manage Cart", "Add Allergen"]
)

# View Flavors
if options == "View Flavors":
    st.header("Available Flavors")
    if st.button("Fetch Flavors"):
        response = requests.get(f"{BASE_URL}/flavors/")
        if response.status_code == 200:
            flavors = response.json()["flavors"]
            if flavors:
                for flavor in flavors:
                    st.subheader(flavor["name"])
                    st.write(f"Ingredients: {', '.join(flavor['ingredients'])}")
                    st.write(f"Availability: {'Yes' if flavor['availability'] else 'No'}")
                    st.write("---")
            else:
                st.info("No flavors available.")
        else:
            st.error("Failed to fetch flavors!")

# Add Flavor
elif options == "Add Flavor":
    st.header("Add a New Flavor")
    with st.form("Add Flavor Form"):
        name = st.text_input("Flavor Name")
        ingredients = st.text_area("Ingredients (comma-separated)")
        submitted = st.form_submit_button("Add Flavor")
        if submitted:
            if name and ingredients:
                ingredients_list = [i.strip() for i in ingredients.split(",")]
                response = requests.post(
                    f"{BASE_URL}/add_flavor/", 
                    json={"name": name, "ingredients": ingredients_list}
                )
                if response.status_code == 200:
                    st.success("Flavor added successfully!")
                elif response.status_code == 400:
                    st.error(response.json()["detail"])
                else:
                    st.error("Failed to add flavor!")
            else:
                st.error("Please fill in all fields!")

# Search Flavors
elif options == "Search Flavors":
    st.header("Search for a Flavor")
    keyword = st.text_input("Enter keyword to search for flavors")
    if st.button("Search"):
        response = requests.get(f"{BASE_URL}/search_flavors/?keyword={keyword}")
        if response.status_code == 200:
            results = response.json()["results"]
            if results:
                for flavor in results:
                    st.subheader(flavor["name"])
                    st.write(f"Ingredients: {', '.join(flavor['ingredients'])}")
                    st.write(f"Availability: {'Yes' if flavor['availability'] else 'No'}")
                    st.write("---")
            else:
                st.info("No flavors found.")
        else:
            st.error("Failed to search flavors!")

# Manage Cart
elif options == "Manage Cart":
    st.header("Manage Your Cart")
    with st.form("Add to Cart Form"):
        flavor_id = st.number_input("Flavor ID to Add to Cart", min_value=1, step=1)
        submitted = st.form_submit_button("Add to Cart")
        if submitted:
            response = requests.post(f"{BASE_URL}/cart/add/", json={"flavor_id": flavor_id})
            if response.status_code == 200:
                st.success("Flavor added to cart successfully!")
            elif response.status_code == 404:
                st.error(response.json()["detail"])
            else:
                st.error("Failed to add flavor to cart!")
    
    if st.button("View Cart"):
        response = requests.get(f"{BASE_URL}/cart/")
        if response.status_code == 200:
            cart = response.json()["cart"]
            if cart:
                for item in cart:
                    st.subheader(item["name"])
                    st.write(f"Ingredients: {', '.join(item['ingredients'])}")
                    st.write("---")
            else:
                st.info("Your cart is empty.")
        else:
            st.error("Failed to fetch cart details!")

# Add Allergen
elif options == "Add Allergen":
    st.header("Add an Allergen")
    with st.form("Add Allergen Form"):
        allergen = st.text_input("Allergen Name")
        submitted = st.form_submit_button("Add Allergen")
        if submitted:
            if allergen:
                response = requests.post(f"{BASE_URL}/add_allergen/", json={"allergen": allergen})
                if response.status_code == 200:
                    st.success("Allergen added successfully!")
                elif response.status_code == 400:
                    st.error(response.json()["detail"])
                else:
                    st.error("Failed to add allergen!")
            else:
                st.error("Please provide an allergen name!")
