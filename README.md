# Discount Codes Api ✈️
A simple api to generate discount codes and fetch discount codes. It is built using python 3.10 and Flask 2.2

## Setup Instruction

* Install the libraries and setup the database

- Setup the Python :snake virtual environment (I have assume that Python is already installed on your system)
  - python3 -m venv simpleapi (this will create a folder name simpleapi, replace it with any other name if you like)
  - goto simpleapi 📁
  - activate the venv by entering this command at command prompt: source bin/activate
  - Install the dependencies
  - pip3 install Flask, Flask-SQLAlchemy, flask-marshmallow (refer to requirement.txt 📄)
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
1. python3 app.py OR
2. flask run

The above command will run the development web server where you test the API endpoints

## API Endpoints
