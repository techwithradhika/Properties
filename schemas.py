from typing import List
from pydantic import BaseModel

class PropertyDetail(BaseModel):
    id: str
    name: str
    address: str
    city: str
    state: str

class PropertyList(BaseModel):
    properties: List[PropertyDetail]
