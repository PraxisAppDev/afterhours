from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from typing import List
from pydantic import BaseModel

class UserException(Exception):
  def __init__(self, message: str):
    self.message = message

async def unhandled_exception_handler(request: Request, exc: Exception):
  return JSONResponse(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    content={
      "message": "server error"
    }
  )

class ValidationErrorModel(BaseModel):
  field_name: str
  message: str

class ValidationErrorsModel(BaseModel):
  validation_errors: List[ValidationErrorModel]

async def validation_exception_handler(request: Request, exc: RequestValidationError):
  print(exc.errors())
  return JSONResponse(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    content=ValidationErrorsModel(
      validation_errors=[
        ValidationErrorModel(
          field_name=field["loc"][1],
          message=str(field["ctx"]["error"]) if field["type"] == "value_error" else field["msg"]
        )
        for field in exc.errors()
      ]
    ).dict()
  )