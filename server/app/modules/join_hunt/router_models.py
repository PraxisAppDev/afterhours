from typing import List, Optional, Union
from datetime import datetime
from pydantic import BaseModel, Field
from app.models import PyObjectId
from app.modules.users.router_models import UserModel

class Join_Hunts_Model(BaseModel):
  id: Optional[PyObjectId] = Field(alias="_id", default=None)
  name: str = Field(...)
  description: str = Field(...)
  huntID: str = Field(...)

  # TODO
  model_config = {
    "json_schema_extra": {
      "examples": [
        {
        }
      ]
    }
  }