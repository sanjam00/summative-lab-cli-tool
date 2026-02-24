

class Project:
  def __init__(self, title, description, due_date, assigned_to):
    self.title = title
    self.description = description
    self.due_date = due_date
    self.assigned_to = assigned_to

  def to_dict(self):
    return {
      "title": self.title,
      "description": self.description,
      "due date": self.due_date,
      "assigned to": self.assigned_to
    }

  def __str__(self):
    # formats the object so it's more readable when it prints
    return str(self.to_dict())