
from pydantic import BaseModel
from app.common.enum import Language
from typing import Optional


class InputHSKUpdateBaseModel(BaseModel):
    id: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "lang": Language.JA,
                "text": "sample text",
            }
        }
