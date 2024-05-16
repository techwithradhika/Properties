from fastapi import FastAPI
from router import property_router

app = FastAPI()
app.include_router(property_router)