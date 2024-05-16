# Properties

This is a simple Note Taking App built with React.js and Django. It allows users to create, view, edit, and delete notes.

Prerequisites
Visual Studio Code.
Python and pip installed.
MangoDB database installed.

Features
1) create_new_property
	Input: property name, address, city, and state.
	Output: list of properties with all details.
2) fetch_property_details
	Input: city name.
	Output: a list of all properties that belong to the city name passed in the input
3) update_property_details
	Input: property_id, property name, address, city, state
	Output: same as create_new_property API with updated information
4) find_cities_by_state: 
  Input: state_id or state_name
  Output: all city names that belong with the state
5) find_similar_properties
		Input: property_id
		Output: list of all properties that belong to the same city as that of given property_id

Technologies Used
Backend: FastAPI
Database: MangoDB

Installation
To run this application locally, follow these steps:

Clone the repository: git clone https://github.com/techwithradhika/Note-Taking-App.git

Navigate to the backend project directory: cd notes_project
Install virtual environment (recommended): pip install virtualenv
Create a virtual environment: python -m virtualenv venv.
Activate the virtual environment: .\venv\Scripts\activate
Install  the dependencies: pip install fastapi pymongo uvicorn
Start server: uvicorn index:app --reload
Access the application in your browser at http://127.0.0.1:8000/docs
