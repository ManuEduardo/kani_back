from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from src.routers import router as kani_router
from src.exceptions import ErrorHandler
from src.database import SessionLocal, engine
from src import models


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.title = "Kani API"
app.version = "0.0.1"
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:5173"
]

options_middleware = {
    "allow_origins" : origins,
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers" : ["*"]
}

app.add_middleware(ErrorHandler)
app.add_middleware(
    CORSMiddleware,
    **options_middleware
)

app.include_router(kani_router)

@app.get("/",include_in_schema=False)
def home():
    return RedirectResponse("/docs")

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response