# Pokedex in Python

# 📌 Summary

The presented code simulates a Pokedex.
The user must enter the name of a Pokemon so through the use of the PokeAPI and the requests library, the program can download information and display it as a search result.

# ⚙️ How it Works
Modules

To properly run the program, the following packages must be installed:   
requests       
pandas   
PIL   

Installation

You can install the dependencies from the terminal using the following commands:   
pip install pandas   
pip install requests   
pip install pillow

# Program Flow

The program works with four main functions:

main   
Requests an input from the user to perform the search and handles errors.
This function makes use of the following functions.

obtain_pokemon   
Uses requests to access the API and saves the retrieved information for further processing.

save_pokemon   
Uses os to check if a folder named pokedex exists.
If it does not exist, it creates it and saves the information from the API in .json format.

show_image   
Uses io and BytesIO to display on screen the image related to the search in the API (the image of the requested Pokémon).

The code includes comments to make it easier to understand.

# Example
![Pokedex](https://github.com/bmayena/Brenda_Mayen_Project_M4_Pokedex/blob/main/pokedex.gif)

# 🚀 Areas for Improvement

The program meets the requested requirements, but the way information is displayed could be improved, for example:

Grouping the data more clearly.

Using tools such as Jupyter Notebook to show the table in a better format.

# 🤖 Use of Artificial Intelligence

This program was modified using ChatGPT, specifically to:

Implement the modules os, io, and PIL.

Improve the formatting of printed information and images on screen.

Reduce errors in the code.

Artificial Intelligence was also used for corrections in the Spanish-to-English translation of this project.
