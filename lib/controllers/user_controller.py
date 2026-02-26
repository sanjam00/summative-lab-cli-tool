from lib.models.user import User
from lib.utils import storage
from .base_controller import BaseController

class UsersController(BaseController):
  def __init__(self, filepath):
    self.filepath = filepath
    self.data = []
  
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

  def list_users(self):
    for user in self.data:
      print(f"[{user._id}] {user.name} <{user.email}>")