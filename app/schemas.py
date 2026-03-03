from pydantic import BaseModel
from typing import List

class HouseFeatures(BaseModel):
    square_footage: float
    bedrooms: int
    bathrooms: int
    year_built: int
    lot_size: float
    distance_to_city_center: float
    school_rating: float


class BatchPredictionRequest(BaseModel):
    houses: List[HouseFeatures]