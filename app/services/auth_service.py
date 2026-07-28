from app.database import db
from app.utils.security import hash_password
from app.utils.security import verify_password, create_access_token 

def create_user(user):
    users = db["users"]

    existing_user = users.find_one({"email": user.email})

    if existing_user:
        return {"error": "User already exists"}

    hashed_password = hash_password(user.password)

    users.insert_one({
        "name": user.name,
        "email": user.email,
        "password": hashed_password
    })

    return {"message": "User created successfully"}

def login_user(user):

    users = db["users"]

    existing_user = users.find_one({"email": user.email})

    if not existing_user:
        return {"error": "User not found"}

    if not verify_password(user.password, existing_user["password"]):
        return {"error": "Invalid password"}

    token = create_access_token(
        {"email": existing_user["email"]}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }