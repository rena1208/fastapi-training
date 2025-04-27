from fastapi import APIRouter
from datetime import datetime
from pydantic import BaseModel

router = APIRouter()

# レスポンスの型
class TimeResponse(BaseModel):
    time: datetime

@router.get('/theme_01', response_model=TimeResponse)
async def get_time():
    time = datetime.now()
    return {"time": time}