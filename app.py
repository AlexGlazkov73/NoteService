import uvicorn

from fastapi import FastAPI

from contextlib import asynccontextmanager

from api import notes
from config import HOST, PORT
from database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(notes)

if __name__ == '__main__':
    uvicorn.run("app:app", host=HOST, port=PORT, reload=True)
