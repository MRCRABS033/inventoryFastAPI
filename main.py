from fastapi import FastAPI
from Models import Product
from typing import List
app = FastAPI()

lista: List[Product] = []

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/item/", response_model=Product)
async def create_item(dto: Product):
    lista.append(dto)
    return dto

@app.get("/item/all", response_model=List[Product])
async def get_all_item():
    return lista
