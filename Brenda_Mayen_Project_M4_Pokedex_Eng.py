# POKEDEX: This program simulates a "pokedex". Through a valid input, it queries and saves information from an API. 
# Later, it processes this information to make it easier to read and handle files.
# Requirements: Run the following in the terminal:
# pip install pandas
# pip install requests
# pip install Pillow

import requests  # to access the API
import json  # to save information in JSON format
import os  # to create folders and files
import pandas as pd  # to format the API information as a table
from PIL import Image  # to display the image on screen
from io import BytesIO

def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:  # code for successful response
        return response.json()
    else:
        return None  # allows showing an error message

def save_pokemon(name, data):
    # Create the json file in a folder called pokedex
    if not os.path.exists("pokedex"):
        os.makedirs("pokedex")
    
    file = f"pokedex/{name.lower()}.json"
    # Make the saved file more readable
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def show_image(image_url):  # Function to display image on screen
    if image_url:
        response = requests.get(image_url)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            image.show()
        else:
            print("An error occurred while downloading the image. Try opening the website directly.")
    else:
        print("No image available for this Pokemon.")

def main():  # Main function
    while True:
        name = input("Enter the name of a Pokemon: ")
        data = get_pokemon(name)

        if data is None:  # Prevents the program from ending if an invalid input is entered
            print("That Pokemon was not found, please try again.\n")
        else:
            # Download info from the API
            info = {
                "weight": data["weight"],
                "height": data["height"],
                "moves": [m["move"]["name"] for m in data["moves"]],
                "abilities": [a["ability"]["name"] for a in data["abilities"]],
                "types": [t["type"]["name"] for t in data["types"]],
                "image": data["sprites"]["front_default"]
            }

            # Create a table with DataFrame
            df = pd.DataFrame({
                "weight": [info["weight"]],
                "height": [info["height"]],
                "moves": [info["moves"]],
                "abilities": [info["abilities"]],
                "types": [info["types"]]
            })

            # Formatting
            df = df.explode("moves").explode("abilities").explode("types")

            print("\n✅ Pokemon found:\n")
            print(df.to_string(index=False))

            save_pokemon(name, info)
            print(f"\n📁  A json file has been created in the Pokedex folder. Open 'pokedex/{name.lower()}.json'")
            print(f"🖼️  The image will be displayed on screen. Image URL: {info['image']}\n")

            # Show image with PIL
            show_image(info["image"])

            break

if __name__ == "__main__":
    main()
