from fastapi import APIRouter, HTTPException
from config.db import session
from models.index import users
from schemas.index import User
from fastapi.responses import JSONResponse


user = APIRouter()


# GET ALL USERS
@user.get("/")
async def read_data():
    # return conn.execute(users.select().fetchall())
    result = session.execute(users.select()).fetchall()
    print(result)
    if result:
        columns = users.c.keys()
        user_list = [dict(zip(columns, row)) for row in result]
        return JSONResponse(user_list)
    else:
        raise HTTPException(status_code=400, detail="failed")
        # return JSONResponse({"message": "failed"})


# GET USER BY ID
@user.get("/{id}")
async def read_data(id: int):
    # return str(conn.execute(users.select(). where(users.c.id == id)).fetchone())

    result = session.execute(users.select().where(users.c.id == id)).fetchone()

    # print(result)

    if result:
        user_data = {"id": result[0], "username": result[1],
                     "password": result[2], "email": result[3]}
        return JSONResponse(user_data)
    else:
        raise HTTPException(status_code=400, detail="User not found")
        return {"message": "failed"}


# INSERT USER
@user.post("/")
async def write_data(user: User):
    result = session.execute(users.insert().values(
        # id=user.id,
        username=user.username,
        email=user.email,
        password=user.password
    ))

    if result.rowcount == 1:
        session.commit()
        inserted_user_id = result.inserted_primary_key[0]
        print("Recieved Data From Frontend")
        print({
            "id": inserted_user_id,
            "username": user.username,
            "email": user.email,
            "password": user.password,
        })
        return JSONResponse({
            "status": "success",
            "data": {
                "id": inserted_user_id,
                "username": user.username,
                "email": user.email,
                "password": user.password,
            }
        })
    else:
        raise HTTPException(
            status_code=500, detail="Failed to insert user data")


# UPDATE USER
@user.put("/{id}")
async def update_user(id: int, user: User):
    update_data = {
        "username": user.username,
        "password": user.password,
        "email": user.email
    }

    result = session.execute(
        users.update().where(users.c.id == id).values(**update_data)
    )

    if result.rowcount == 1:
        session.commit()
        return JSONResponse({
            "status": "success",
            "message": update_data
        })
    else:
        raise HTTPException(
            status_code=404, detail=f"User with ID {id} not found")


# DELETE USER
@user.delete("/{id}")
async def delete_data(id: int):
    user_to_delete = session.execute(
        users.select().where(users.c.id == id)).fetchone()
    print(user_to_delete)
    result = session.execute(users.delete().where(users.c.id == id))
    # return conn.execute(users.select()).fetchall()

    if result.rowcount == 1:
        session.commit()
        # inserted_user_id = result.inserted_primary_key[0]
        return JSONResponse({
            "status": "success",
            "deleted_user": {
                "id": id,
                "username": user_to_delete.username,
                "email": user_to_delete.email,
                "password": user_to_delete.password,
            }
        })
    else:
        raise HTTPException(
            status_code=500, detail="Failed to delete user data")
