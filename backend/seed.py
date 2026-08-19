import os

from dotenv import load_dotenv
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.role import Role
from app.models.user import User
from app.core.security import hash_password

load_dotenv()

def seed_roles(db: Session):
    
    roles = [
        "Super Admin",
        "Admin",
        "Manager",
        "Employee"
    ]
    
    for role_name in roles:
        existing_role = db.query(Role).filter(Role.name == role_name).first()
        
        if not existing_role:
            db.add(Role(name = role_name))
            
    db.commit()
    

def seed_super_admin(db: Session):
    email = os.getenv("SUPER_ADMIN_EMAIL")
    password = os.getenv("SUPER_ADMIN_PASSWORD")
    
    if not email or not password:
        raise ValueError("SUPER_ADMIN_EMAIL and SUPER_ADMIN_PASSWORD")
    
    existing_user = db.query(User).filter(User.email == email).first()
    
    if existing_user:
        print("Super Admin already exists.")
        return
    
    super_admin_role = db.query(Role).filter(Role.name == "Super Admin").first()
    
    if not super_admin_role:
        raise ValueError("Super Admin role not found")
    
    hashed_pw = hash_password(password)
    
    
    super_admin = User(
        full_name = "Super Admin",
        email = email,
        password_hash = hashed_pw,
        role_id = super_admin_role.role_id,
        is_active = True
    )
    
    db.add(super_admin)
    db.commit()
    
    print("Super Admin created successfully")
    
def main():
    db = SessionLocal()
    
    try:
        seed_roles(db)
        seed_super_admin(db)
    finally:
        db.close()
        
        
if __name__ == "__main__":
    main()
    
    
    

 