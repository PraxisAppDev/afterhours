from fastapi import FastAPI
from app.modules.users import router as users
from app.modules.hunts import router as hunts
from app.modules.teams import router as teams
from app.exceptions import unhandled_exception_handler, validation_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    '*'
]

app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
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

app.include_router(
    teams.router,
    prefix="/teams",
    tags=["Teams"]
)