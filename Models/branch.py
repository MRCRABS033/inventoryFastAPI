from pydantic import BaseModel, Field


class branch(BaseModel):
    name: str = Field(..., description="Name")
    address: str = Field(..., description="Address")
