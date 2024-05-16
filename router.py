from fastapi import APIRouter, HTTPException
from bson import ObjectId
from db import properties_collection as collection
from schemas import PropertyDetail, PropertyList
from models import Property

property_router = APIRouter() 

@property_router.post('/create_new_property', response_model=PropertyDetail)
async def create_new_property(property: Property):
    property_dict = property.dict()
    property_id = collection.insert_one(property_dict).inserted_id
    inserted_property = collection.find_one({"_id": property_id})
    if not inserted_property:
        raise HTTPException(status_code=500, detail="Failed to create property")
    return PropertyDetail(id=str(inserted_property['_id']), **inserted_property)

@property_router.get('/fetch_property_details', response_model=PropertyList)
async def fetch_property_details(city: str):
    properties = list(collection.find({"city": city}))
    if not properties:
        raise HTTPException(status_code=404, detail="Properties not found")
    property_list = []
    for property in properties:
        property_list.append(PropertyDetail(id=str(property['_id']), **property))
    return PropertyList(properties=property_list)

@property_router.put('/update_property_details', response_model=PropertyDetail)
async def update_property_details(property_id: str, property: Property):
    updated_property = collection.find_one_and_update(
        {"_id": ObjectId(property_id)},
        {"$set": property.dict()},
        return_document=True
    )
    if not updated_property:
        raise HTTPException(status_code=404, detail="Property not found")
    return PropertyDetail(id=str(updated_property['_id']),**updated_property)

@property_router.get('/find_cities_by_state')
async def find_cities_by_state(state: str):
    cities = list(collection.distinct("city", {"state": state}))
    if not cities:
        raise HTTPException(status_code=404, detail="No cities found for the given state")
    return {"cities": cities}

@property_router.get('/find_similar_properties', response_model=PropertyList)
async def find_similar_properties(property_id: str):
    property_details = collection.find_one({"_id": ObjectId(property_id)})
    if not property_details:
        raise HTTPException(status_code=404, detail="Property not found")
    city = property_details.get("city")
    similar_properties = list(collection.find({"city": city}))
    property_list = []
    for property in similar_properties:
        property_list.append(PropertyDetail(id=str(property['_id']), **property))
    return PropertyList(properties=property_list)