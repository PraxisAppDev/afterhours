from pydantic import BaseModel, Field, field_validator
from enum import Enum
from email_validator import validate_email, EmailNotValidError
import re

class SignUpModel(BaseModel):
  username: str = Field(
    description="The username of the user. Most be unique. Must be between 3 and 20 characters long.",
    min_length=3, 
    max_length=20
  )
  fullname: str = Field(
    description="The full name of the user. Must be between 3 and 1024 characters long.",
    min_length=3, 
    max_length=1024
  )
  email: str = Field(
    description="The user's email address. Must be a valid email address.",
    min_length=3,
    max_length=254, # 254 is the maximum length of an email address by IETF standards
  )
  password: str = Field(
    description="The password of the user. Must have 8 or more characters, one number and one special character. Alternatively, must be at least 16 characters long. Must be less than 72 characters.",
    min_length=8, 
    max_length=72, 
    # can't use pattern because I don't want to implement this without lookaheads
    # pattern="^(([a-zA-Z0-9!@#$%^&*(),.?\":{}|<>]{16,72})|((?=.*[0-9])(?=.*[!@#$%^&*(),.?\":{}|<>])[a-zA-Z0-9!@#$%^&*(),.?\":{}|<>]{8,72}))$"
  )

  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "username": "testy tester",
          "email": "random@gmail.com",
          "fullname": "Test Testy",
          "password": "randompassword123"
        }
      ],
    }
  }

  # @field_validator("username")
  # def username_validator(cls, value):
  #   if len(value) < 3:
  #     raise ValueError("username must be at least 3 characters long")
  #   elif len(value) > 20:
  #     raise ValueError("username must be less than 20 characters long")
  #   else:
  #     return value

  @field_validator("fullname")
  def fullname_validator(cls, value):
    if len(value) < 3:
      raise ValueError("Fullname must be at least 3 characters long")
    elif len(value) > 1024:
      raise ValueError("Fullname must be less than 1024 characters long")
    else:
      return value
  
  @field_validator("password")
  def password_validator(cls, value):
    if len(value) < 8:
      raise ValueError("Password must be at least 8 characters long")
    elif len(value) > 72:
      raise ValueError("Password must be less than 72 characters long")
    elif len(value) >= 16:
      return value
    elif not re.search(r"[0-9]", value):
      raise ValueError("Password must contain at least one number")
    elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
      raise ValueError("Password must contain at least one special character")
    else:
      return value

  @field_validator("email")
  def email_validator(cls, value):
    try:
      validate_email(value, check_deliverability=False)
    except EmailNotValidError as e:
      raise ValueError("Email is not valid: " + str(e))
    return value
  
  def get_normalized_email(self):
    emailInfo = validate_email(self.email, check_deliverability=False)
    return emailInfo.normalized


class LoginModel(BaseModel):
  username: str = Field(
    description="The username of the user. Most be unique. Must be between 3 and 20 characters long.",
    min_length=3, 
    max_length=20
  )
  password: str = Field(
    description="The password of the user. Must have 8 or more characters, one number and one special character. Alternatively, must be at least 16 characters long. Must be less than 72 characters.",
    min_length=8, 
    max_length=72,
  )
  # no need for a validator here past length constraints because the email is already validated in the SignUpModel

  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "username": "testy tester",
          "password": "randompassword123"
        }
      ]
    }
  }

class Token(BaseModel):
  access_token: str = Field(
    description="A JWT token to be used for authentication.",
    pattern=r"^[A-Za-z0-9_-]{2,}(?:\.[A-Za-z0-9_-]{2,}){2}$"
  )
  exp: str = Field(
    description="Expiration date for client"
  )
  token_type: str = "bearer"

  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "access_token": "<a_token>",
          "exp": "2019-05-18T15:17:08",
          "token_type": "bearer"
        }
      ]
    }
  }

class AuthSuccessTextModel(str, Enum):
  LOGIN_SUCCESSFUL = "login successful"
  SIGNUP_SUCCESSFUL = "signup successful"

class AuthSuccessModel(BaseModel):
  message: AuthSuccessTextModel = Field(
    description="A message about the success of the authentication operation."
  )
  token: Token = Field(
    description="A JWT token to be used for authentication."
  )

  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "message": "login successful",
          "token": {
            "access_token": "<a_token>",
            "exp": "2019-05-18T15:17:08",
            "token_type": "bearer"
          }
        }
      ]
    }
  }

class AuthErrorTextModel(str, Enum):
  INCORRECT_CREDENTIALS = "Incorrect Email or Password. Please try again."
  INTERNAL_SERVER_ERROR = "Internal Server Error: error creating user"
  USER_ALREADY_EXISTS = "User already exists"

class AuthErrorModel(BaseModel):
  message: AuthErrorTextModel = Field(
    description="A message about the failure of the authentication operation."
  )

  model_config = {
    "json_schema_extra": {
      "examples": [
        {
          "message": AuthErrorTextModel.INCORRECT_CREDENTIALS
        },
        {
          "message": AuthErrorTextModel.INTERNAL_SERVER_ERROR
        },
        {
          "message": AuthErrorTextModel.USER_ALREADY_EXISTS
        }
      ]
    }
  }