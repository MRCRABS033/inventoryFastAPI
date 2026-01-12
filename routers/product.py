from typing import List
from Models import product
from fastapi import APIRouter

router = APIRouter(prefix="/product", tags=["product"])

lista = List[product]
@router.get("/", response_model=List[product])
async def get_all() -> type[list[product]]:
    return lista

@router.get("/{id}", response_model=product)
async def get_by_id(id: int) -> product:
    producto = product(id=id, name="Producto", price=10.50, stock=10, SKU="2025")
    return producto
