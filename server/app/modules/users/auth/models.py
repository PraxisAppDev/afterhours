from pydantic import BaseModel
class SignUpModel(BaseModel):
  username: str
  email: str
  fullname: str
  password: str

  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "username": "testy tester",
          "email": "random@gmail.com",
          "fullname": "Test Testy",
          "password": "randompassword"
        }
      ]
    }
  }

class LoginModel(BaseModel):
  email: str
  password: str

  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "email": "random@gmail.com",
          "password": "randompassword"
        }
      ]
    }
  }

class AuthResponseModel(BaseModel):
  message: str
  token: str

  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "message": "login successful",
          "token": "random-jwt-token"
        }
      ]
    }
  }

class TokenModel(BaseModel):
  access_token: str
  token_type: str

class TokenDataModel(BaseModel):
  id: str | None = None