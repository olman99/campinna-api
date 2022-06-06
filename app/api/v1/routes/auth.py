from fastapi import APIRouter, Body

router = APIRouter(
    prefix="/auth",
    tags=['Authentication'],
    responses={401: {'description': 'Unauthorized'},
               404: {'description': 'User not found'}}
)


@router.post("/login")
async def login(username: str = Body(), password: str = Body()):
    pass
