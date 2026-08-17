from fastapi import FastAPI

from app.routers.role import router as role_router

app = FastAPI(
    title="LeaveTrack API",
    description="Employee Leave Management System",
    version="1.0.0"
)

app.include_router(role_router)

@app.get("/")

def root():
    return{
        "message": "LeaveTrack API is running successfully"
    }