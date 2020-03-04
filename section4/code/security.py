from user import User

users = [
   User(1, "bob", "asdf")
]

username_mapping = { u.username: u for u in users} #this is an object with a list comprehension inside of it, that produces a key with the username and the full object at the value
userid_mapping = { u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload["identity"]
    return userid_mapping.get(user_id, None)