from fastapi import APIRouter
from bson import ObjectId

from models.user import User
from config.db import db
from schemas.user import userEntity, usersEntity

user = APIRouter()

@user.get('/')
async def find_all_users():
    # print(db.local.user.find())
    # print(usersEntity(db.local.user.find()))
    return usersEntity(db.local.user.find())

@user.post('/')
async def create_users(user: User):
    db.local.user.insert_one(dict(user))
    return usersEntity(db.local.user.find())

@user.get('/{id}')
async def find_one_user(id):
    return userEntity(db.local.user.find_one({"_id": ObjectId(id)}))

@user.put('/{id}')
async def update_user(id, user: User):
    db.local.user.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(user)
    })

    return userEntity(db.local.user.find_one({"_id": ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id):
    return userEntity(db.local.user.find_one_and_delete({"_id": ObjectId(id)}))
