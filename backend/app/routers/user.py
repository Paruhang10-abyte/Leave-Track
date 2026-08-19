from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services import (
    create_user,
    get_user_by_email,
    get_user_by_id, 
    get_all_users,
    update_user
)

from app.services import user as user_service

router = APIRouter(
    prefix= "/users",
    tags = ["Users"]
)

@router.post("/register", response_model=UserResponse)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    
    existing_user = get_user_by_email(db, user.email)
    
    if existing_user:
        raise HTTPException(status_code= 400, detail= "Email already registered")
    
    return create_user(db, user)


@router.get("/", response_model= list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    
    return get_all_users(db)
    
    
@router.get("/{user_id}", response_model= UserResponse)
def get_user(
    user_id: int, 
    db: Session = Depends(get_db)
):
    
    user = get_user_by_id(db, user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@router.patch("/{user_id}", response_model= UserResponse)
def user_update(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):
    
    user = get_user_by_id(db, user_id)
    
    if not user:
        raise HTTPException(status_code= 404, detail= "User not found")
    
    return update_user(db, user, user_data)