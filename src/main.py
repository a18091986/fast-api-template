from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from api import router as api_router
from core.config import settings
from core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(api_router, prefix=settings.api_prefix.prefix)

@app.get("/")
def read_root():
    return {"message": "Hello World"}   


if __name__ == "__main__":
    uvicorn.run(app="main:app", 
                host=settings.server.host, 
                port=settings.server.port, 
                reload=True)