from pydantic import BaseModel

class SignUpModel(BaseModel):
  username: str
  email: str
  fullname: str
  password: str

class LoginModel(BaseModel):
  email: str
  password: str

class TokenModel(BaseModel):
  access_token: str
  token_type: str

class TokenDataModel(BaseModel):
  id: str | None = None