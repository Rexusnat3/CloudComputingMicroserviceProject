from fastapi import APIRouter

router = APIRouter(prefix="/route", tags=["Route"])
@router.get("/")
async def create_route():
    return {"message": "endpoint functions succesfully"}
