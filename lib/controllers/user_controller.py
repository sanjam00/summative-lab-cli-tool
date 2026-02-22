from lib.models.user import User

class UsersController:

  def __init__(self, filepath):
    self.filepath = filepath
    self.data = []
  
  def add_user(self, args):
    if any(u.email == args.email for u in self.data):
      print(f"User with email {args.email} already exists.")
    
    #MVC - model, view, controller
    user = User(name=args["name"], email=args["email"])
    self.data.append(user)

    print(f"User {user.name} was added successfully with ID: {user._id}")

    return user
