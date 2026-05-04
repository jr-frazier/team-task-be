from fastapi import FastAPI
from app.routers import tasks
from app.database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Task Board API",
    description="A simple task board API",
    version="0.1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)


@app.get("/healthy")
def health_check():
    return {"status": "Healthy"}

app.include_router(tasks.router)