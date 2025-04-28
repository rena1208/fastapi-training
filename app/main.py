from fastapi import FastAPI

from .themes import theme_01, theme_02, theme_03, theme_04

app = FastAPI()

app.include_router(theme_01.router, prefix="/themes")
app.include_router(theme_02.router, prefix="/themes")
app.include_router(theme_03.router, prefix="/themes")
app.include_router(theme_04.router, prefix="/themes")

@app.get("/health")
def health():
    return {"status": "ok"}
