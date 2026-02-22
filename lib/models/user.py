import uuid

class User:
  def __init__(self, name, email, user_id=None):
    self.name = name
    self.email = email
    self._id = user_id if not user_id else uuid.uuid4()
      #private variable means hands off, leave alone

  def  to_dict(self):
    return {
      "id": self._id,
      "name": self.name,
      "email": self.email
    }

  @classmethod
  def from_dict(cls, data):
    return cls(name=data.get("name"), email=data.get("email"), user_id=data.get("id"))
  