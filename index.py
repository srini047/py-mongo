from fastapi import  FastAPI

# Routes
from routes.user import user

app = FastAPI()

app.include_router(user)
