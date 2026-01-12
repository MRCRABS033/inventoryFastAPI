from typing import List
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
async def hello():
    return {"message": "Hello World"}