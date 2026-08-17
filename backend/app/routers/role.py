from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.role import Role
from app.schemas.role import RoleCreate, RoleUpdate


router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)

@router.post("/")
def create_role(role:RoleCreate, db: Session = Depends(get_db)):
    
    new_role = Role(
        name=role.name, 
        description=role.description
    )  
    
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    
    return {
        "message": "Role created successfully", 
        "role": new_role
    }
    
@router.get("/")
def get_roles(db: Session = Depends(get_db)):
    
    roles = db.query(Role).all()
    
    return{
        "message": "Roles retrieved successfully", 
        "roles": roles
    }
    
@router.get("/{role_id}")
def get_role(role_id: int, db: Session = Depends(get_db)):
    
    role = db.query(Role).filter(Role.role_id == role_id).first()
    
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    return(
        {
            "message": "Role retrieved successfully",
            "role": role
        }
    )
    
@router.patch("/{role_id}")
def update_role(
    role_id: int,
    role: RoleUpdate,
    db: Session = Depends(get_db)
):
    
    existing_role = db.query(Role).filter(Role.role_id == role_id).first()
    
    if not existing_role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    if role.name is not None:
        existing_role.name = role.name
        
    if role.description is not None:
        existing_role.description = role.description
        
    if role.is_active is not None:
        existing_role.is_active = role.is_active
        
    db.commit()
    db.refresh(existing_role)
        
    return{
        "message": "Role updated Successfully",
        "role": existing_role
    }
    
@router.delete("/{role_id}")
def delete_role(role_id: int,db: Session = Depends(get_db)):
    
    existing_role = db.query(Role).filter(Role.role_id == role_id).first()
    
    if not existing_role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    existing_role.is_active = False
    db.commit()
    
    return{
        "message": "Role deleted successfully"
    }