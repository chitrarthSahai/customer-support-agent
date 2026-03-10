from main import AppFactory

app = AppFactory.create_app()


@app.get("/users")
async def get_users():
    # Placeholder for fetching users from a database or service
    return {"users": ["Alice", "Bob", "Charlie"]}


@app.post("/users")
async def create_user(user: dict):
    # Placeholder for creating a new user in a database or service
    return {"message": f"User {user['name']} created successfully"}


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    # Placeholder for fetching a specific user by ID from a database or service
    return {"user": {"id": user_id, "name": f"User{user_id}"}}


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: dict):
    # Placeholder for updating a specific user by ID in a database or service
    return {"message": f"User {user_id} updated successfully"}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    # Placeholder for deleting a specific user by ID from a database or service
    return {"message": f"User {user_id} deleted successfully"}
