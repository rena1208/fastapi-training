from fastapi import FastAPI

from .themes import analyze_geojson, get_fibonacci, present_time, random_tile

app = FastAPI()

app.include_router(present_time.router, prefix="/themes")
app.include_router(get_fibonacci.router, prefix="/themes")
app.include_router(random_tile.router, prefix="/themes")
app.include_router(analyze_geojson.router, prefix="/themes")

@app.get("/health")
def health():
    return {"status": "ok"}
