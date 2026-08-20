from datetime import datetime

from pydantic import BaseModel, ConfigDict

class RoleCreate(BaseModel):
    name:str
    description:str | None = None
    is_active:bool | None = None
    
class RoleUpdate(BaseModel):
    name:str | None = None
    description:str | None = None
    is_active:bool | None = None
    
class RoleResponse(BaseModel):
    role_id: int
    name:str
    description:str | None
    is_active:bool
    created_at:datetime
    updated_at:datetime
    
    model_config = ConfigDict(from_attributes=True)
    