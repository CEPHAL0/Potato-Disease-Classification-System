from pydantic import BaseModel


class ModelOutput(BaseModel):
    class_: str
    confidence: float
