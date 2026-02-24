from lib.models.user import User
from lib.utils import storage
from .base_controller import BaseController

class UsersController(BaseController):
  def __init__(self, filepath):
    self.filepath = filepath
    self.data = []
  
  # def __enter__(self):
  #   # allow an object to be used with the with statement.
  #   self.data = [User.from_dict(user) for user in storage.load_data(self.filepath)]
  #   return self

  # def __exit__(self, exc_type, exc, tb):
  #   # allow an object to be used with the with statement.
  #   storage.save_data(self.filepath, [user.to_dict() for user in self.data])

  model_class = User

  def add_user(self, args):
    if any(u.email == args["email"] for u in self.data):
      print(f"User with email {args['email']} already exists.")
      return None
    
    #MVC - model, view, controller
    user = User(name=args["name"], email=args["email"])
    self.data.append(user)

    print(f"User {user.name} was added successfully with ID: {user._id}")

    return user

  def list_user(self):
    for user in self.data:
      print(f"[{user._id}] {user.name} <{user.email}>")