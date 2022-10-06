# Discount Codes Api ✈️
A simple api to generate discount codes and fetch discount codes. It is built using python 3.10 and Flask 2.2

## Setup Instruction

* Install the libraries and setup the database

- Setup the Python :snake virtual environment (I have assume that Python is already installed on your system)
  - ```python3 -m venv simpleapi``` (this will create a folder name simpleapi, replace it with any other name if you like)
  - goto simpleapi 📁
  - activate the venv by entering this command at command prompt: ```source bin/activate```
  - Install the dependencies
  - ```pip3 install Flask, Flask-SQLAlchemy, flask-marshmallow``` (refer to requirement.txt 📄)
- Lets run the app 💻


## Database Commands
SQLite database loyality.db is used by the app. During development/testing you can create the Database, Drop it and Seed it with initial data

| Action         | Command                       |
|---------------:|-------------------------------|
| Create Database| flask --app db_setup db_create|
| Drop Database  | flask --app db_setup db_drop  |
| Seed Database  | flask --app db_setup db_seed  |

Note: commands should be entered in simpleap folder at command prompt

## Run the App
1. ```python3 app.py``` OR
2. ```flask run```

The above command will run the development web server **http://localhost:5000** where you test the API endpoints

## API Endpoints

| API endpoint | Description |
|--------------|-------------|
| http://localhost:5000/brands | Return the brands defined in the DB |
| http://localhost:5000/codes  | Return all the discount for all the brands |
| http://localhost:5000/codes?brand_id=2 | Return all the codes of brand_id=2 <br /> There are 3 brands defined in the DB having ids 1,2 and 3|
| **http://localhost:5000/generate_disc_codes?brand_id=1&count=20**|  It will generate the 20 discount codes for the brand_id=2 <br /> You can pass other values 2 or 3 for brand_id, count is optional by default it will generate 10 codes or you can pass any positive number <br />This endpoint expects two parameters brand_id and count i.e. number of codes to generate. |
| **http://localhost:5000/fetch_discount_code?brand_id=1&user_id=2** |  It fetch a discount for a user for a brand. <br />This endpoint expects two parameters brand_id and user_id (there are two users defined in the DB with id 1 and 2 |


Happy Programming! 🌛

