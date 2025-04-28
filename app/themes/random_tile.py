from  fastapi import APIRouter
import random
import httpx
from fastapi.responses import Response

router = APIRouter()

tile_urls = [
    "https://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png",
    "https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png",
    "https://cyberjapandata.gsi.go.jp/xyz/blank/{z}/{x}/{y}.png",
    "https://cyberjapandata.gsi.go.jp/xyz/seamlessphoto/{z}/{x}/{y}.jpg"
]

@router.get("/tiles/{z}/{x}/{y}")
async def get_random_tile(z: int, x: int, y: int):
    # ランダムなタイルURLを選択
    tile_template = random.choice(tile_urls)
    tile_url = tile_template.format(z=z, x=x, y=y)

    async with httpx.AsyncClient() as client:
        response = await client.get(tile_url)

    if response.status_code != 200:
        return Response(content="tileが見つかりませんでした", status_code=404)

    return Response(content=response.content, media_type="image/png")