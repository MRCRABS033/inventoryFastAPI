import datetime
from typing import List
from .product import Product
from pydantic import BaseModel, Field

class orderModel(BaseModel):
    destination: str = Field(..., description="The destination of the order")
    departure_time_origin: str = Field(..., description="The departure time of the order")
    id: int = Field(..., description="The id of the order")
    name: str = Field(..., description="The name of the order")
    active: bool = Field(..., description="Whether the order is active")
    modified: bool = Field(..., description="Whether the order is modified")
    products: List[Product] | Product = Field(..., description="The products of the order")