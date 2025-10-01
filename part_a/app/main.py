# part_a/app/main.py
from fastapi import FastAPI
from app.db.database import init_db
from app.api.routers import router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    await init_db()
    yield
    # (Optional) Add shutdown cleanup here


app = FastAPI(
    title="OriGen Simulation Scheduler",
    lifespan=lifespan
)

# Include API routes
app.include_router(router, prefix="/api")
