from fastapi import FastAPI
from app.modules.users import router as users
from app.modules.hunts import router as hunts
from app.modules.auth import router as auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    # TODO
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Auth"]
)

app.include_router(
    users.router,
    prefix="/users",
    tags=["Users"]
)

app.include_router(
    hunts.router,
    prefix="/hunts",
    tags=["Hunts"]
)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}