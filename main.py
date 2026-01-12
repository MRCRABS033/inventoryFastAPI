from fastapi import FastAPI
from routers import product as product_router
from routers import UsersRoute as users_router
from Models import product
from typing import List
app = FastAPI()
app.include_router(product_router.router)
app.include_router(users_router.router)
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
