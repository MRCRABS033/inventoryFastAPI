from pydantic import BaseModel, Field
class product(BaseModel):
    id: int = Field(..., description="The id of the product")
    name: str = Field(...)
    SKU: str = Field(...)
    price: float = Field(description="The price of the product")
    stock: int = Field(description="The quantity of the product")