from fastapi import Request
from fastapi.responses import JSONResponse

class UserException(Exception):
  def __init__(self, message: str):
    self.message = message

async def unhandled_exception_handler(request: Request, exc: Exception):
  return JSONResponse(
    status_code=500,
    content={
      "message": "server error"
    }
  )