

class Project:
  def __init__(self, title, description, due_date, assigned_to, complete=False):
    self.title = title
    self.description = description
    self.due_date = due_date
    self.assigned_to = assigned_to
    self.complete = complete

  def to_dict(self):
    return {
      "title": self.title,
      "description": self.description,
      "assigned to": self.assigned_to,
      "due date": self.due_date,
      "complete": self.complete,
    }

  def __str__(self):
    # formats the object so it's more readable when it prints
    return str(self.to_dict())
  
  @classmethod
  def from_dict(cls, data):
    return cls(title=data.get("title"), description=data.get("description"), assigned_to=data.get("assigned to"), due_date=data.get("due date"), complete=data.get("complete"))