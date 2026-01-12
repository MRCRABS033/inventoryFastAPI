from pydantic import BaseModel, Field

class pser(BaseModel):
    id: int = Field(..., description="The id of the user")
    name: str = Field(...)
    active: bool = Field(...)
    password: str = Field(...)