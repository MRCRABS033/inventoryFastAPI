from pydantic import BaseModel, Field
class Product(BaseModel):
    name: str = Field(...)
    price: float = Field(description="The price of the product")
    quantity: int = Field(description="The quantity of the product")