from fastapi import FastAPI
import models
from database.database import engine
from routers import device, library

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(device.router)
app.include_router(library.router)
