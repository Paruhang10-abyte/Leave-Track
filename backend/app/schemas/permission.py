from datetime import datetime

from pydantic import BaseModel, ConfigDict

class PermissionCreate(BaseModel):
    name:str
    description: str | None = None
    is_active: bool | None = None
    
class PermissionUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    is_active: bool | None = None

class PermissionResponse(BaseModel):
    permission_id: int
    name: str
    description: str | None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
    