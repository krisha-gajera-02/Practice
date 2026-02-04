import json
import os

file_name = "users.json"

if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        json.dump({"users": []}, f, indent=4)

def create_user(user_id, name, age):
    with open(file_name, "r") as f:
        data = json.load(f)
    data["users"].append({"id": user_id, "name": name, "age": age})
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)
    print(f"User {name} created")

def read_users():
    with open(file_name, "r") as f:
        data = json.load(f)
    print("\nAll Users:")
    for user in data["users"]:
        print(user)

def update_user(user_id, name=None, age=None):
    with open(file_name, "r") as f:
        data = json.load(f)

    user_found = False

    for user in data["users"]:
        if user["id"] == user_id:
            if name is not None:
                user["name"] = name
            if age is not None:
                user["age"] = age
            user_found = True
            print(f"User {user_id} updated")
            break

    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

def delete_user(user_id):
    with open(file_name, "r") as f:
        data = json.load(f)
    new_users = [user for user in data["users"] if user["id"] != user_id]
    if len(new_users) == len(data["users"]):
        print(f"User {user_id} not found")
    else:
        data["users"] = new_users
        print(f"User {user_id} deleted")
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

create_user(1, "Krisha", 18)
create_user(2, "Aditi", 19)

read_users()

update_user(1, name="Krisha Gajera", age=18)

read_users()

delete_user(2)

read_users()
