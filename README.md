# Discount Codes Api ✈️

## What it does?
It is a small part of a customer loyality app. It has 2️⃣ microservices accessible via REST API: 1) Generate Discount Coderuns 2) Fetch discount code for a user. 

## What it consist of?
A development web server and two microservices ✈️

## Development stack?
Python 3.10, Flask 2.2 (web framework), SQLAlchemy (ORM) and Marshmallow (serialization). In this project SQLite database is used that can be replaced with other database type.

## Setup Instruction

Note: these instructions are for Mac OS

- Create a parent working folder
- Goto that folder and clone the repository. It will create a folder discount_api_codes
- Setup the Python 🐍 virtual environment (I have assumed that Python 3.x is already installed on your system)
  - ```
  python3 -m venv discount_codes_api
  cd discount_codes_api
  source bin/activate  (for Mac OS and Linux)  
  ``` 
- Install the libraries and setup the database
  - goto discount_codes_api 📁
  - Install the dependencies
  - ```pip3 install flask, flask-SQLAlchemy, flask-marshmallow, marshmallow-sqlalchemy ``` (refer to requirement.txt 📄)
- Create the database, Seed the database (refer to next section)
- Lets run the app 💻 and test the endpoints using Postman 🏤 or web browser 🌍
  ```
  flask run
  ```


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

The above command will run the development web server **http://localhost:5000** where you can test the API endpoints

## API Endpoints

| API endpoint | Description |
|--------------|-------------|
| http://localhost:5000/brands | Return the brands 🛍️ list defined in the DB |
| http://localhost:5000/codes  | Return all the discount codes 💸 for all the brands |
| http://localhost:5000/codes?brand_id=2 | Return all the discount codes of brand_id=2 <br /> There are 3 brands defined in the DB having ids 1, 2 and 3|
| **http://localhost:5000/generate_disc_codes?brand_id=1&count=20**|  It will generate the 20 discount codes for the brand_id=2 <br /> You can pass other values 2 or 3 for brand_id. The *count* is optional, by default it will generate 🔟 codes or you can pass any positive number. <br />This endpoint expects 2️⃣ parameters: brand_id and count (i.e. number of codes to generate.) |
| **http://localhost:5000/fetch_discount_code?brand_id=1&user_id=2** |  It fetches a discount code 🎟️ for a user of a brand. <br />This endpoint expects 2️⃣ parameters brand_id and user_id (there are two users defined in the DB with id 1 and 2 |


Happy Programming! 🌛
Fawad

