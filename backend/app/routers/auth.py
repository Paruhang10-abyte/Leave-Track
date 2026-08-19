from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.auth import LoginRequest
from app.services.auth import authenticate_user
from app.core.jwt import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/login")
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    
    user = authenticate_user(db, login_data.email, login_data.password)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    
    access_token = create_access_token(
        data={"sub": str(user.user_id)}
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
    
    
    