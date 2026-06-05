
from pydantic import BaseModel

class PositionData(BaseModel):
    lat: float
    lng: float
    topic: str

class TakingOffData(BaseModel):
    topic: str

class LandingData(BaseModel):
    topic: str
