
class Task:
  def __init__(self, title, complete=False):
    self.title = title
    self.complete = complete

  def  to_dict(self):
    return {
      "title": self.title,
      "complete": self.complete
    }
  
  def __str__(self):
    # formats the object so it's more readable when it prints
    return str(self.to_dict())
  
  @classmethod
  def from_dict(cls, data):
    return cls(title=data.get("title"), complete=data.get("complete"))