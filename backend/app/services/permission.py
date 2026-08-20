from sqlalchemy.orm import Session

from app.models.permission import Permission
from app.schemas.permission import PermissionCreate, PermissionUpdate

def create_permission(
    db: Session,
    permission_data: PermissionCreate
):
    
    new_permission = Permission(
        name=permission_data.name,
        description=permission_data.description,
        is_active=(
            permission_data.is_active
            if permission_data.is_active is not None
            else True
        )
    )
    
    db.add(new_permission)
    db.commit()
    db.refresh(new_permission)

    return new_permission

def get_all_permissions(db: Session):
    return db.query(Permission).all()


def get_permission_by_id(
    db: Session,
    permission_id: int
):
    return (
        db.query(Permission)
        .filter(Permission.permission_id == permission_id)
        .first()
    )
    
def update_permission(
    db: Session,
    permission: Permission,
    permission_data: PermissionUpdate
):
    if permission_data.name is not None:
        permission.name = permission_data.name

    if permission_data.description is not None:
        permission.description = permission_data.description

    if permission_data.is_active is not None:
        permission.is_active = permission_data.is_active

    db.commit()
    db.refresh(permission)

    return permission

def delete_permission(
    db: Session,
    permission: Permission
):
    permission.is_active = False

    db.commit()
    db.refresh(permission)

    return permission
    
