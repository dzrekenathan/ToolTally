from fastapi import APIRouter, Depends, HTTPException, status
# from ....schemas.user import UserCreate, UserOut, UserStatus
# from ....core.authentication.auth_middleware import get_current_user
from app.core.authentication.auth_middleware import get_current_active_user, get_current_user
from app.models import models
from app.schemas.user import UserOut


router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_current_user(current_user: models.User = Depends(get_current_active_user)):
    try:
        return current_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))