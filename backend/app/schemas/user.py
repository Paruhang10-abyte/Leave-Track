from pydantic import BaseModel, EmailStr, Field

PASSWORD_PATTERN = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*!]).*$"

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str = Field(
        min_length=8, 
        max_length=128,
        pattern= PASSWORD_PATTERN
    )
    role_id: int
    
class UserUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None

class ChangePassword(BaseModel):
    old_password: str
    new_password: str = Field(
        min_length=8,
        max_length=128,
        pattern= PASSWORD_PATTERN
    )
    
class UserResponse(BaseModel):
    user_id: int
    full_name: str
    email: EmailStr
    role_id: int
    is_active: bool
    
    model_config = {"from_attributes": True}
    