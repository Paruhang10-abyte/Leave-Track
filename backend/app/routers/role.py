from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.role import RoleCreate, RoleUpdate, RoleResponse
from app.services.role import (
    create_role,
    get_all_roles,
    get_role_by_id,
    update_role,
    delete_role
)

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


@router.post("/", response_model=RoleResponse)
def create_new_role(
    role: RoleCreate,
    db: Session = Depends(get_db)
):
    return create_role(db, role)


@router.get("/", response_model=list[RoleResponse])
def get_roles(
    db: Session = Depends(get_db)
):
    return get_all_roles(db)


@router.get("/{role_id}", response_model=RoleResponse)
def get_role(
    role_id: int,
    db: Session = Depends(get_db)
):
    role = get_role_by_id(db, role_id)

    if not role:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    return role


@router.patch("/{role_id}", response_model=RoleResponse)
def update_existing_role(
    role_id: int,
    role_data: RoleUpdate,
    db: Session = Depends(get_db)
):
    role = get_role_by_id(db, role_id)

    if not role:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    return update_role(db, role, role_data)


@router.delete("/{role_id}")
def deactivate_role(
    role_id: int,
    db: Session = Depends(get_db)
):
    role = get_role_by_id(db, role_id)

    if not role:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    delete_role(db, role)

    return {
        "message": "Role deleted successfully"
    }