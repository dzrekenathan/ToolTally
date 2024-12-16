from fastapi import FastAPI
from app.api.v1.routers import login, post, register, user
from .models import models
from .core.database import engine



models.Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(user.router)
app.include_router(register.router)
app.include_router(login.router)
app.include_router(post.router)

@app.get('/')
async def root():
    return {"message": "Hello World"}