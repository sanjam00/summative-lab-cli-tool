from lib.models.user import User
from lib.utils import storage

class UsersController:
  def __init__(self, filepath):
    self.filepath = filepath
    self.data = []
  
  def __enter__(self):
    self.data = [User.from_dict(user) for user in storage.load_data(self.filepath)]
    return self

  def __exit__(self, exc_type, exc, tb):
    storage.save_data(self.filepath, [user.to_dict() for user in self.data])

  def add_user(self, args):
    if any(u.email == args["email"] for u in self.data):
      print(f"User with email {args["email"]} already exists.")
      return None
    
    #MVC - model, view, controller
    user = User(name=args["name"], email=args["email"])
    self.data.append(user)

    print(f"User {user.name} was added successfully with ID: {user._id}")

    return user

  def list_user(self):
    for user in self.data:
      print(f"[{user._id}] {user.name} <{user.email}>")