from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hashed_password

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()

def create_user(db: Session, user: UserCreate):
    hashed_pw = hashed_password(user.password)
    
    new_user = User(
        full_name = user.full_name,
        email= user.email,
        hashed_password = hashed_pw,
        role_id = user.role_id,
        is_active = True
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user