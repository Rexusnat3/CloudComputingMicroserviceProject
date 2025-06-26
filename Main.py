from fastapi import FastAPI
from Routers import Route


app = FastAPI()
app.include_router(Route.router)