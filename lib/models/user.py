import uuid

class User:
  def __init__(self, name, email, user_id=None):
    self.name = name
    self.email = email
    if not user_id:
      self._id = str(uuid.uuid4())
    else:
      self._id = user_id
      #private variable means hands off, leave alone

  def  to_dict(self):
    return {
      "id": self._id,
      "name": self.name,
      "email": self.email
    }

  def __str__(self):
    # formats the object so it's more readable when it prints
    return str(self.to_dict())

  @classmethod
  def from_dict(cls, data):
    return cls(name=data.get("name"), email=data.get("email"), user_id=data.get("id"))
  