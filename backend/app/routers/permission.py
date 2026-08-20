from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 

from app.db.database import get_db
from app.schemas.permission import(
    PermissionCreate,
    PermissionUpdate,
    PermissionResponse
)

from app.services.permission import(
    create_permission,
    get_all_permissions,
    get_permission_by_id,
    update_permission,
    delete_permission
)

router = APIRouter(
    prefix="/permissions",
    tags=["Permissions"]
)

@router.post("/", response_model=PermissionResponse)
def create_new_permission(
    permission: PermissionCreate,
    db: Session = Depends(get_db)
):
    return create_permission(db, permission)

@router.get("/", response_model=list[PermissionResponse])
def get_permissions(
    db: Session = Depends(get_db)
):
    return get_all_permissions(db)

@router.get("/{permission_id}", response_model=PermissionResponse)
def get_permission(
    permission_id: int,
    db: Session = Depends(get_db)
):
    
    permission = get_permission_by_id(db, permission_id)
    
    if not permission:
        raise HTTPException(status_code=404, detail= "Permission not found")
    
    return permission

@router.patch("/{permission_id}", response_model=PermissionResponse)
def update_existing_permission(
    permission_id: int,
    permission_data: PermissionUpdate,
    db: Session = Depends(get_db)
):
    
    
    permission = get_permission_by_id(db, permission_id)
    
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    
    return update_permission(db,permission, permission_data)

@router.delete("/{permission_id}")
def deactivate_permission(
    permission_id: int,
    db: Session = Depends(get_db)
):
    
    permission = get_permission_by_id(db, permission_id)
    
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    
    delete_permission(db, permission)
    
    return {
        "message": "Permission deleted succesfully"
    }