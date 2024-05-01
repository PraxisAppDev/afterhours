from typing import List, Optional, Union
from datetime import datetime
from pydantic import BaseModel, Field, field_validator
from app.models import PyObjectId
from email_validator import validate_email, EmailNotValidError
from enum import Enum

phone_number_regex = r"^(\+\d{1,3} )?(((\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4})|(\d{5} \d{5})|\d{6,15})(, ?\d{1,4})?$"


class UserModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    username: str = Field(...)
    email: str = Field(...)
    phone: Union[None, str] = Field(
        None,
        description="The user's phone number.",
        pattern=phone_number_regex
    )
    fullname: str = Field(...)
    lastLogin: datetime = Field(...)
    huntHistory: List[PyObjectId] = []

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "test",
                    "email": "test@gmail.com",
                    "phone": "123-456-7890",
                    "fullname": "testy tester",
                    "lastLogin": "2024-02-19T10:30:00Z",
                    "huntHistory": []
                }
            ]
        }
    }


class UserCreateModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    username: str = Field(...)
    email: str = Field(...)
    # Removed so phone field isn't generated on user creation
    # phone: Union[None, str] = Field(
    #   None,
    #   description="The user's phone number.",
    #   pattern=phone_number_regex
    # )
    fullname: str = Field(...)
    hashedPassword: str = Field(...)
    lastLogin: datetime = Field(...)
    huntHistory: List[PyObjectId] = []

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "test",
                    "email": "test@gmail.com",
                    "phone": "123-456-7890",
                    "fullname": "testy tester",
                    "lastLogin": "2024-02-19T10:30:00Z",
                    "huntHistory": []
                }
            ]
        }
    }


class UpdateUserModel(BaseModel):
    username: Optional[str] = Field(None)
    # not using a regex because email validation is relatively complex
    email: Optional[str] = Field(None, min_length=3, max_length=254)
    phone: Optional[str] = Field(None, pattern=phone_number_regex)
    fullname: Optional[str] = Field(None)
    lastLogin: Optional[datetime] = Field(None)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "test",
                    "email": "test@gmail.com",
                    "phone": "123-456-7890",
                    "fullname": "testy tester",
                    "huntId": "23d3f6fccdcd5a3917558d43",
                    "lastLogin": "2024-02-19T10:30:00Z"
                }
            ]
        }
    }

    @field_validator("email")
    def email_validator(cls, value):
        try:
            validate_email(value)
            return value
        except EmailNotValidError as e:
            raise ValueError("Email is not valid: " + str(e))


# enum
class UserResponseTextModel(str, Enum):
    USER_NOT_FOUND = "user not found"
    USER_FOUND = "found user"
    USER_UPDATED = "updated user"
    USER_DELETED = "deleted user"
    HUNTS_FOUND = "found hunts"


class UserResponseModel(BaseModel):
    message: UserResponseTextModel
    # TODO Change the last one to List of Hunts later
    content: Union[List[UserModel], UserModel, str, bool, List[PyObjectId]]
