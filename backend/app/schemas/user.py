from pydantic import BaseModel, EmailStr, Field, field_validator


def validate_password_strength(value: str) -> str:
    if not any(c.islower() for c in value):
        raise ValueError("Password must contain a lowercase letter")

    if not any(c.isupper() for c in value):
        raise ValueError("Password must contain an uppercase letter")

    if not any(c.isdigit() for c in value):
        raise ValueError("Password must contain a digit")

    if not any(c in "@#$%^&*!" for c in value):
        raise ValueError("Password must contain a special character")

    return value


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)
    role_id: int

    _validate_password = field_validator("password")(
        validate_password_strength
    )


class UserUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None


class ChangePassword(BaseModel):
    old_password: str
    new_password: str = Field(
        min_length=8,
        max_length=72
    )

    _validate_password = field_validator("new_password")(
        validate_password_strength
    )


class UserResponse(BaseModel):
    user_id: int
    full_name: str
    email: EmailStr
    role_id: int
    is_active: bool

    model_config = {"from_attributes": True}