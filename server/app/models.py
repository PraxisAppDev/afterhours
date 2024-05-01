# Global models, might rename to utils

from typing import Annotated
from pydantic import BeforeValidator

# Represents an ObjectId field in the database.
PyObjectId = Annotated[str, BeforeValidator(str)]