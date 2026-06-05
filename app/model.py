
from pydantic import BaseModel

class PositionData(BaseModel):
    lat: float
    lng: float
    topic: str
