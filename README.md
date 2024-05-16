#  Property Management API

This API provides endpoints for managing properties, including creating new properties, fetching property details, updating property information, and finding similar properties.

# Prerequisites

- Visual Studio Code.
- Python and pip installed.
- MangoDB installed.

## Features

- **Create new property :**
   input: property name, address, city, and state.
   Output: list of properties with all details.
- **fetch property details :**
   Input: city name.
   Output: a list of all properties that belong to the city name passed in the input
- **update property details :**
  Input: property_id, property name, address, city, state
  Output: same as create_new_property API with updated information
- **find_cities_by_state :** 
Input: state_id or state_name
Output: all city names that belong with the state
- **find_similar_properties :** 
    Input: property_id
    Output: list of all properties that belong to the same city as that of given property_id

## Installation

To run this project locally, follow these steps:

1. Clone the repository: git clone https://github.com/techwithradhika/Properties.git
2. Navigate to the current project directory: cd Properties
3. Install virtual environment (recommended): pip install virtualenv
4. Create a virtual environment: python -m virtualenv venv
5. Activate the virtual environment: .\venv\Scripts\activate
6. Install Django and other backend dependencies: pip install fastapi pymongo uvicorn
7. Start the FastAPI server: uvicorn app:app --reload (Note: Make sure MongoDB server is running).
8. The server will start running at http://127.0.0.1:8000, access the api Endpoints at http://127.0.0.1:8000/docs .
