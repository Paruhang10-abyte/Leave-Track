from sqlalchemy.orm import Session

from app.models.role import Role
from app.schemas.role import RoleCreate, RoleUpdate


def create_role(db: Session, role_data: RoleCreate):
    new_role = Role(
        name=role_data.name,
        description=role_data.description,
        is_active=role_data.is_active
    )

    db.add(new_role)
    db.commit()
    db.refresh(new_role)

    return new_role


def get_all_roles(db: Session):
    return db.query(Role).all()


def get_role_by_id(db: Session, role_id: int):
    return db.query(Role).filter(Role.role_id == role_id).first()


def update_role(db: Session, role: Role, role_data: RoleUpdate):
    if role_data.name is not None:
        role.name = role_data.name

    if role_data.description is not None:
        role.description = role_data.description

    if role_data.is_active is not None:
        role.is_active = role_data.is_active

    db.commit()
    db.refresh(role)

    return role


def delete_role(db: Session, role: Role):
    role.is_active = False

    db.commit()
    db.refresh(role)

    return role