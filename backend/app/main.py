from fastapi import FastAPI

from app.routers.role import router as role_router
from app.routers.user import router as user_router
from app.routers.auth import router as auth_router

app = FastAPI(
    title="LeaveTrack API",
    description="Employee Leave Management System",
    version="1.0.0"
)

app.include_router(role_router)
app.include_router(user_router)
app.include_router(auth_router)

@app.get("/")

def root():
    return{
        "message": "LeaveTrack API is running successfully"
    }