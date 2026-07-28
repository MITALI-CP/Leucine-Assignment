from fastapi import APIRouter
from app.models.user import UserSignup
from app.services.auth_service import create_user
from app.models.user import UserSignup, UserLogin
from app.services.auth_service import create_user, login_user

router = APIRouter()


@router.post("/signup")
def signup(user: UserSignup):
    return create_user(user)

@router.post("/login")
def login(user: UserLogin):
    return login_user(user)