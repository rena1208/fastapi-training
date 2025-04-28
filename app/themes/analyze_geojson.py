from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any, List

router = APIRouter()

# リクエストの型
class GeoJSONRequest(BaseModel):
    type: str
    features: List[Dict[str, Any]]

# レスポンスの型
class GeoJSONResponse(BaseModel):
    feature_count: int
    properties_count: int

@router.post("/analyze", response_model=GeoJSONResponse)
async def analyze_geojson(data: GeoJSONRequest):
    feature_count = len(data.features)
    properties_count = sum(len(feature.get("properties", {})) for feature in data.features)

    return GeoJSONResponse(
        feature_count=feature_count,
        properties_count=properties_count
    )