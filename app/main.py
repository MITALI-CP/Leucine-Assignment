from fastapi import FastAPI,Depends
from app.routes.auth import router as auth_router
from app.utils.auth import verify_token
from app.routes.document import router as document_router
from app.routes.chat import router as chat_router
app = FastAPI(
    title="Leucine Backend Assignment",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(document_router)
app.include_router(chat_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to Leucine Backend Assignment"
    }
    
@app.get("/profile")
def profile(user=Depends(verify_token)):
    return {
        "message": "Welcome to your profile",
        "user": user
    }    