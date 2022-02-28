def userEntity(item) -> dict:   # Single User
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"]
    }

def usersEntity(entity) -> list:    # Array of Users
    return [userEntity((item)) for item in entity]

# def serializeDict(sd) -> dict:
#     return {**{i:str(sd[i]) for i in sd if (i == }_id)}, **{}}
